__all__ = 'TyrvingDataM TyrvingDataF tyrvingPoints'

from athlib.utils import parse_hms

class TyrvingDataM:
	gender = 'M'

	def __init__(self, event_code, kind, *args):
		self.event_code = event_code	#so we can talk about it
		self.kind = kind	#race jump pv & throw
		self.args = args

	def calculate_points(self, age, perf, timing_kind='automatic'):
		meth = getattr(self,self.kind+'_points',self.bad_points)
		self.timing_kind = timing_kind
		age = int(age)
		return meth(age, perf)

	@property
	def ident(self):
		return '%s(%r,%r,%r)' % (self.__class__.__name__, self.event_code, self.gender, self.kind)

	def bad_points(self, *args, **kwds):
		raise ValueError('cannot compute points for %s' % self.ident)

	def get_base_perf(self, age, yv):
		if isinstance(yv,dict):
			base_perf = yv.get(age,None)
		else:
			y, v = yv
			base_perf = v[age-y] if y<=age<y+len(v) else None
		if base_perf is None:
			raise ValueError('cannot obtain base performance for %s at age=%s' % (self.ident,age))
		return base_perf

	def race_points(self, age, perf):
		dist, multiplier, yv = self.args
		base_perf = self.get_base_perf(age,yv)

		#perf is a time
		v = perf
		if not isinstance(v,(int,float)):
			perf.replace(',','.')
			while v.count('.')>1: v = v.replace('.',':',1)
			v = parse_hms(v) if ':' in v else float(v)

		timing_kind = self.timing_kind

		if self.timing_kind=='manual':
			inc = 0.24 if dist in (100,110,200) else 0.20 if dist in (40,60,80,300) else 0.14 if dist == 400 else 0
			v += inc #correct for manual timing

		return max(0,int(1000 + 1e-8 + (base_perf - v) * (multiplier / (0.01 if dist<=500 else 0.1))))

	def jump_points(self, age, perf):
		multiplier, yv = self.args
		base_perf = self.get_base_perf(age,yv)

		#perf is a distance
		if not isinstance(v,(int,float)):
			v = float(perf.replace(',','.'))
		return max(0,1000 + 1e-8 + multiplier * (v - base_perf) / 100.0)	#ie per centimetre

	def stav_points(self, arge, perf):
		'''this works for all the piecewise linear distance events'''
		multipliers, yvs = self.args

		levels = [self.get_base_perf(age,yv) for yv in yvs]
		if not isinstance(v,(int,float)):
			v = float(perf.replace(',','.'))
		diffs = 100*(v - levels[0]), 100*(v - levels[1])
		return max(0, 1000 + 1e-8 + diffs[0]*multipliers[0] if diffs[0]>=0
						else diffs[0]*multipliers[1] if diffs[1]>0 
						else diffs[1]*multipliers[2]+levels[2]-1000)
	throw_points = stav_points
	pv_points = stav_points

class TyrvingDataF(TyrvingDataM):
	gender = 'F'

def tyrvingPoints(gender, age, event_code, perf, timing_kind='automatic'):
	obj = _tyrvingTables.get(gender.upper(),None)
	if obj is None:
		raise ValueError('Cannot get a Tyrving table for gender=%r' % gender)
	obj = obj.get(event_code,None)
	if not obj:
		raise ValueError('Cannot get a Tyrving calculation for gender=%r event_code=%r' % (gender, event_code))
	return obj.calculate_points(age, perf, timing_kind=timing_kind)


#these are obtained using scripts/tyrving-translate
_tyrvingTables = {
  'M':{
    '40': TyrvingDataM('40', 'race', *(40, 3.5, (10, (6.6, 6.4)))),
    '60': TyrvingDataM('60', 'race', *(60, 2.7, (10, (9.2, 8.8, 8.4, 8, 7.75,
       7.55, 7.4, 7.3, 7.25, 7.2)))),
    '80': TyrvingDataM('80', 'race', *(80, 2.2, (10, (12.15, 11.55, 10.9, 10.4,
       10.05, 9.8, 9.6, 9.45, 9.35, 9.3)))),
    '100': TyrvingDataM('100', 'race', *(100, 1.7, (12, (13.5, 12.8, 12.35,
       11.95, 11.7, 11.5, 11.35, 11.25)))),
    '200': TyrvingDataM('200', 'race', *(200, 0.85, (11, (29.2, 27.6, 26, 24.8,
       24, 23.5, 23, 22.65, 22.5)))),
    '300': TyrvingDataM('300', 'race', *(300, 0.6, (12, (45, 42, 40, 38.6,
       37.6, 36.85, 36.45, 36.15)))),
    '400': TyrvingDataM('400', 'race', *(400, 0.4, (14, (56.5, 54.3, 52.5,
       51.5, 51, 50.4)))),
    '600': TyrvingDataM('600', 'race', *(600, 2.6, (10, (112, 105, 99, 94.5,
       91, 88.5, 86, 84, 83, 82)))),
    '800': TyrvingDataM('800', 'race', *(800, 1.8, (14, (129, 124, 120, 117.5,
       115.5, 114)))),
    '1000': TyrvingDataM('1000', 'race', *(1000, 1.1, (14, (169, 164, 159, 156,
       153, 150)))),
    '1500': TyrvingDataM('1500', 'race', *(1500, 0.7, (12, (294, 278, 268, 260,
       252, 246, 242, 240)))),
    '2000': TyrvingDataM('2000', 'race', *(2000, 0.45, (14, (380, 365, 355,
       346, 341, 338)))),
    '3000': TyrvingDataM('3000', 'race', *(3000, 0.27, (16, (552, 540, 530,
       523)))),
    '5000': TyrvingDataM('5000', 'race', *(5000, 0.15, (17, (950, 930, 910)))),
    '10000': TyrvingDataM('10000', 'race', *(10000, 0.06, (18, (1980, 1950)))),
    '1000W': TyrvingDataM('1000W', 'race', *(1000, 0.7, (11, (320, 300, 282,
       271, 262, 254, 246, 242, 240)))),
    '2000W': TyrvingDataM('2000W', 'race', *(2000, 0.3, (13, (594, 570, 548,
       531, 518, 510, 505)))),
    '3000W': TyrvingDataM('3000W', 'race', *(3000, 0.18, (13, (924, 892, 854,
       830, 810, 796, 788)))),
    '5000W': TyrvingDataM('5000W', 'race', *(5000, 0.11, (14, (1600, 1500,
       1440, 1395, 1365, 1350)))),
    '10000W': TyrvingDataM('10000W', 'race', *(10000, 0.05, (15, (3180, 3060,
       2960, 2890, 2850)))),
    '20000W': TyrvingDataM('20000W', 'race', *(20000, 0.02, (18, (6000,
       5880)))),
    '60H 68.0cm 6.5m': TyrvingDataM('60H 68.0cm 6.5m', 'race', *(60, 2, (10,
       (11.3, 10.5)))),
    '60H 76.2cm 7m': TyrvingDataM('60H 76.2cm 7m', 'race', *(60, 2, (12, (10.2
      )))),
    '60H 76.2cm 7.5m': TyrvingDataM('60H 76.2cm 7.5m', 'race', *(60, 2, (13,
       (9.8)))),
    '80H 84.0cm 8m': TyrvingDataM('80H 84.0cm 8m', 'race', *(80, 1.4, (14,
       (12.05)))),
    '100H 84.0cm 8.5m': TyrvingDataM('100H 84.0cm 8.5m', 'race', *(100, 1.1,
       (15, (14)))),
    '100H 91.4cm 8.5m': TyrvingDataM('100H 91.4cm 8.5m', 'race', *(100, 1.1,
       (16, (14.5)))),
    '110H 91.4cm 9.14m': TyrvingDataM('110H 91.4cm 9.14m', 'race', *(110, 1,
       (17, (15.3)))),
    '110H 100.0cm 9.14m': TyrvingDataM('110H 100.0cm 9.14m', 'race', *(110, 1,
       (17, (15.8, 15.3, 15)))),
    '110H 106.7cm 9.14m': TyrvingDataM('110H 106.7cm 9.14m', 'race', *(110, 1,
       (18, (15.7, 15.4)))),
    '200H 68.0cm 18.29m': TyrvingDataM('200H 68.0cm 18.29m', 'race', *(200,
       0.6, (11, (34.8, 32.8, 31.2)))),
    '200H 76.2cm 18.29m': TyrvingDataM('200H 76.2cm 18.29m', 'race', *(200,
       0.6, (14, (29.2, 28.4, 27.6, 27, 26.5, 26)))),
    '300H 76.2cm 35m': TyrvingDataM('300H 76.2cm 35m', 'race', *(300, 0.46,
       (14, (44.7, 43)))),
    '300H 84.0cm 35m': TyrvingDataM('300H 84.0cm 35m', 'race', *(300, 0.46,
       (16, (41.8, 41)))),
    '300H 91.4cm 35m': TyrvingDataM('300H 91.4cm 35m', 'race', *(300, 0.46,
       (18, (40.5, 40)))),
    '400H 84.0cm 35m': TyrvingDataM('400H 84.0cm 35m', 'race', *(400, 0.34,
       (17, (57)))),
    '400H 91.4cm 35m': TyrvingDataM('400H 91.4cm 35m', 'race', *(400, 0.34,
       (18, (56, 55.5)))),
    '1500SC': TyrvingDataM('1500SC', 'race', *(1500, 0.55, (14, (300, 288,
       280)))),
    '2000SC': TyrvingDataM('2000SC', 'race', *(2000, 0.41, (17, (385, 375,
       370)))),
    '3000SC': TyrvingDataM('3000SC', 'race', *(3000, 0.27, (17, (610, 595,
       585)))),
    'HJ': TyrvingDataM('HJ', 'jump', *(7, (10, (1.25, 1.38, 1.5, 1.61, 1.72,
       1.8, 1.88, 1.93, 1.96, 1.99)))),
    'SHJ': TyrvingDataM('SHJ', 'jump', *(8.5, (10, (1, 1.1, 1.2, 1.29, 1.37,
       1.44, 1.5, 1.55, 1.59, 1.61)))),
    'PV': TyrvingDataM('PV', 'pv', *([1.7, 3.5, 7],
       [(10, (2, 2.3, 2.6, 2.9, 3.2, 3.5, 3.8, 4.05, 4.3, 4.5)),
       (10, (1.6, 1.84, 2.08, 2.32, 2.56, 2.8, 3.04, 3.24, 3.44, 3.6)),
       (10, (860, 839, 818, 797, 776, 755, 734, 716, 699, 685))])),
    'LJ': TyrvingDataM('LJ', 'jump', *(2, (10, (4.15, 4.55, 4.95, 5.35, 5.75,
       6.15, 6.4, 6.6, 6.8, 6.95)))),
    'SLJ': TyrvingDataM('SLJ', 'jump', *(5, (10, (2.1, 2.28, 2.45, 2.6, 2.75,
       2.88, 2.98, 3.05, 3.1, 3.15)))),
    'TJ': TyrvingDataM('TJ', 'jump', *(1, (10, (8.2, 9.2, 10.1, 11.1, 12, 12.8,
       13.3, 13.7, 14, 14.3)))),
    'SP6': TyrvingDataM('SP6', 'throw', *([0.3, 0.6, 1.2],
       [(18, (14.6, 15.2)), (18, (11.68, 12.16)), (18, (824, 817))])),
    'SP5': TyrvingDataM('SP5', 'throw', *([0.3, 0.6, 1.2],
       [(16, (14.6, 15.8)), (16, (11.68, 12.64)), (16, (824, 810))])),
    'SP4': TyrvingDataM('SP4', 'throw', *([0.3, 0.6, 1.2],
       [(14, (13.3, 15.3)), (14, (10.64, 12.24)), (14, (840, 816))])),
    'SP3': TyrvingDataM('SP3', 'throw', *([0.3, 0.6, 1.2],
       [(12, (11.3, 13.5)), (12, (9.04, 10.8)), (12, (864, 838))])),
    'SP2': TyrvingDataM('SP2', 'throw', *([0.3, 0.6, 1.2], [(10, (8.5, 10.5)),
       (10, (6.8, 8.4)), (10, (898, 874))])),
    'DT1.75': TyrvingDataM('DT1.75', 'throw', *([0.13, 0.25, 0.5],
       [(18, (46, 48)), (18, (36.8, 38.4)), (18, (770, 760))])),
    'DT1.5': TyrvingDataM('DT1.5', 'throw', *([0.13, 0.25, 0.5],
       [(16, (45, 48)), (16, (36, 38.4)), (16, (775, 760))])),
    'DT1': TyrvingDataM('DT1', 'throw', *([0.13, 0.25, 0.5], [(14, (44, 51)),
       (14, (35.2, 40.8)), (14, (780, 745))])),
    'DT0.75': TyrvingDataM('DT0.75', 'throw', *([0.13, 0.25, 0.5],
       [(12, (32, 40)), (12, (25.6, 32)), (12, (840, 800))])),
    'DT0.6': TyrvingDataM('DT0.6', 'throw', *([0.13, 0.25, 0.5],
       [(10, (22, 28)), (10, (17.6, 22.4)), (10, (890, 860))])),
    'HT6': TyrvingDataM('HT6', 'throw', *([0.1, 0.2, 0.4], [(18, (56, 62)),
       (18, (44.8, 49.6)), (18, (776, 752))])),
    'HT5': TyrvingDataM('HT5', 'throw', *([0.1, 0.2, 0.4], [(16, (52, 59)),
       (16, (41.6, 47.2)), (16, (792, 764))])),
    'HT4': TyrvingDataM('HT4', 'throw', *([0.1, 0.2, 0.4], [(14, (41, 50)),
       (14, (32.8, 40)), (14, (836, 800))])),
    'HT3': TyrvingDataM('HT3', 'throw', *([0.1, 0.2, 0.4], [(13, (37)),
       (13, (29.6)), (13, (852))])),
    'HT2': TyrvingDataM('HT2', 'throw', *([0.1, 0.2, 0.4],
       [(10, (22, 30, 38)), (10, (17.6, 24, 30.4)), (10, (912, 880, 848))])),
    'JT800': TyrvingDataM('JT800', 'throw', *([0.1, 0.2, 0.4],
       [(18, (59, 62)), (18, (47.2, 49.6)), (18, (764, 752))])),
    'JT700': TyrvingDataM('JT700', 'throw', *([0.1, 0.2, 0.4],
       [(16, (55, 60)), (16, (44, 48)), (16, (780, 760))])),
    'JT600': TyrvingDataM('JT600', 'throw', *([0.1, 0.2, 0.4],
       [(14, (46, 52)), (14, (36.8, 41.6)), (14, (816, 792))])),
    'JT400': TyrvingDataM('JT400', 'throw', *([0.1, 0.2, 0.4],
       [(10, (25, 32, 38, 45)), (10, (20, 25.6, 30.4, 36)),
       (10, (900, 872, 848, 820))])),
    'OT150': TyrvingDataM('OT150', 'throw', *([0.08, 0.15, 0.3],
       [(10, (48, 55, 63, 70, 80)), (10, (38.4, 44, 50.4, 56, 64)),
       (10, (856, 835, 811, 790, 760))])),
    'BT1': TyrvingDataM('BT1', 'throw', *([0.08, 0.15, 0.3],
       [(10, (24, 30, 36)), (10, (19.2, 24, 28.8)), (10, (928, 910, 892))]))
  },
  'F':{
    '40': TyrvingDataF('40', 'race', *(40, 3.5, (10, (6.6, 6.4)))),
    '60': TyrvingDataF('60', 'race', *(60, 2.7, (10, (9.25, 8.85, 8.55, 8.4,
       8.25, 8.15, 8.05, 8, 7.95, 7.9)))),
    '80': TyrvingDataF('80', 'race', *(80, 2.1, (10, (12.2, 11.6, 11.1, 10.85,
       10.65, 10.5, 10.35, 10.25, 10.15, 10.1)))),
    '100': TyrvingDataF('100', 'race', *(100, 1.6, (12, (13.8, 13.4, 13.1,
       12.9, 12.75, 12.6, 12.5, 12.4)))),
    '200': TyrvingDataF('200', 'race', *(200, 0.78, (11, (29.7, 28.5, 27.7,
       27.1, 26.5, 26.15, 25.9, 25.7, 25.55)))),
    '300': TyrvingDataF('300', 'race', *(300, 0.5, (12, (45.8, 44.5, 43.4,
       42.5, 41.7, 41.2, 40.8, 40.5)))),
    '400': TyrvingDataF('400', 'race', *(400, 0.38, (14, (61.6, 60, 58.8, 58,
       57.5, 57)))),
    '600': TyrvingDataF('600', 'race', *(600, 2.4, (10, (115, 110, 105, 102,
       100, 98.5, 97, 96, 95, 94)))),
    '800': TyrvingDataF('800', 'race', *(800, 1.5, (14, (141, 138.5, 136, 134,
       133, 132.5)))),
    '1000': TyrvingDataF('1000', 'race', *(1000, 1, (14, (189, 186.5, 184,
       181.5, 180, 179)))),
    '1500': TyrvingDataF('1500', 'race', *(1500, 0.6, (12, (315, 305, 295, 286,
       282, 279, 277, 275)))),
    '2000': TyrvingDataF('2000', 'race', *(2000, 0.4, (14, (418, 406, 398, 393,
       389, 385)))),
    '3000': TyrvingDataF('3000', 'race', *(3000, 0.23, (16, (625, 615, 607,
       600)))),
    '5000': TyrvingDataF('5000', 'race', *(5000, 0.13, (17, (1080, 1065,
       1055)))),
    '10000': TyrvingDataF('10000', 'race', *(10000, 0.06, (18, (2310, 2280)))),
    '1000W': TyrvingDataF('1000W', 'race', *(1000, 0.7, (11, (320, 303, 288,
       280, 275, 272, 270, 268, 266)))),
    '2000W': TyrvingDataF('2000W', 'race', *(2000, 0.3, (13, (640, 620, 600,
       588, 578, 574, 570)))),
    '3000W': TyrvingDataF('3000W', 'race', *(3000, 0.18, (13, (1002, 962, 936,
       920, 906, 900, 895)))),
    '5000W': TyrvingDataF('5000W', 'race', *(5000, 0.1, (14, (1660, 1615, 1585,
       1555, 1538, 1524)))),
    '10000W': TyrvingDataF('10000W', 'race', *(10000, 0.05, (15, (3540, 3450,
       3390, 3330, 3300)))),
    '20000W': TyrvingDataF('20000W', 'race', *(20000, 0.02, (18, (3210,
       3120)))),
    '60H 68.0cm 6.5m': TyrvingDataF('60H 68.0cm 6.5m', 'race', *(60, 1.9, (10,
       (11.6, 10.9)))),
    '60H 76.2cm 7m': TyrvingDataF('60H 76.2cm 7m', 'race', *(60, 1.9, (12,
       (10.5)))),
    '60H 76.2cm 7.5m': TyrvingDataF('60H 76.2cm 7.5m', 'race', *(60, 1.9, (13,
       (10.1, 9.7)))),
    '80H 76.2cm 8m': TyrvingDataF('80H 76.2cm 8m', 'race', *(80, 1.4, (15,
       (12.5, 12.2)))),
    '100H 76.2cm 8.5m': TyrvingDataF('100H 76.2cm 8.5m', 'race', *(100, 1, (17,
       (15)))),
    '100H 84.0cm 8.5m': TyrvingDataF('100H 84.0cm 8.5m', 'race', *(100, 1, (18,
       (14.9, 14.7)))),
    '200H 68.0cm 19m': TyrvingDataF('200H 68.0cm 19m', 'race', *(200, 0.5, (11,
       (36, 34, 32.4)))),
    '200H 76.2cm 19m': TyrvingDataF('200H 76.2cm 19m', 'race', *(200, 0.5, (14,
       (31.6, 31, 30.4, 30, 29.7, 29.5)))),
    '300H 76.2cm 35m': TyrvingDataF('300H 76.2cm 35m', 'race', *(300, 0.4, (14,
       (48, 47, 46.4, 45.9, 45.5, 45.2)))),
    '400H 76.2cm 35m': TyrvingDataF('400H 76.2cm 35m', 'race', *(400, 0.3, (18,
       (63.1, 62.5)))),
    '1500SC': TyrvingDataF('1500SC', 'race', *(1500, 0.46, (14, (340, 330,
       325)))),
    '2000SC': TyrvingDataF('2000SC', 'race', *(2000, 0.35, (17, (430, 420,
       410)))),
    '3000SC': TyrvingDataF('3000SC', 'race', *(3000, 0.2, (17, (700, 670,
       650)))),
    'HJ': TyrvingDataF('HJ', 'jump', *(7.5, (10, (1.22, 1.34, 1.44, 1.52, 1.58,
       1.61, 1.64, 1.66, 1.68, 1.7)))),
    'SHJ': TyrvingDataF('SHJ', 'jump', *(9.5, (10, (1, 1.1, 1.2, 1.26, 1.3,
       1.33, 1.35, 1.36, 1.37, 1.38)))),
    'PV': TyrvingDataF('PV', 'pv', *([2, 4, 8],
       [(10, (1.8, 2, 2.2, 2.5, 2.8, 2.95, 3.1, 3.2, 3.3, 3.4)),
       (10, (1.44, 1.6, 1.76, 2, 2.24, 2.36, 2.48, 2.56, 2.64, 2.72)),
       (10, (856, 840, 824, 800, 776, 764, 752, 744, 736, 728))])),
    'LJ': TyrvingDataF('LJ', 'jump', *(2.1, (10, (4.1, 4.35, 4.7, 5, 5.25,
       5.36, 5.47, 5.55, 5.63, 5.7)))),
    'SLJ': TyrvingDataF('SLJ', 'jump', *(6, (10, (2.05, 2.18, 2.3, 2.4, 2.48,
       2.54, 2.59, 2.62, 2.64, 2.66)))),
    'TJ': TyrvingDataF('TJ', 'jump', *(1, (10, (8, 8.8, 9.5, 10.2, 10.8, 11.4,
       11.9, 12.2, 12.4, 12.6)))),
    'SP4kg': TyrvingDataF('SP4kg', 'throw', *([0.3, 0.6, 1.2],
       [(18, (11.4, 11.7)), (18, (9.12, 9.36)), (18, (863, 859))])),
    'SP3': TyrvingDataF('SP3', 'throw', *([0.3, 0.6, 1.2],
       [(14, (10.8, 11.4, 12, 12.6)), (14, (8.64, 9.12, 9.6, 10.08)),
       (14, (870, 863, 856, 848))])),
    'SP2': TyrvingDataF('SP2', 'throw', *([0.3, 0.6, 1.2],
       [(10, (6.8, 8.8, 10.2, 11.2)), (10, (5.44, 7.04, 8.16, 8.96)),
       (10, (918, 894, 877, 865))])),
    'DT1': TyrvingDataF('DT1', 'throw', *([0.15, 0.3, 0.6],
       [(16, (37, 40, 42, 43)), (16, (29.6, 32, 33.6, 34.4)),
       (16, (778, 760, 748, 742))])),
    'DT0.75': TyrvingDataF('DT0.75', 'throw', *([0.15, 0.3, 0.6],
       [(14, (38, 43)), (14, (30.4, 34.4)), (14, (772, 742))])),
    'DT0.6': TyrvingDataF('DT0.6', 'throw', *([0.15, 0.3, 0.6],
       [(10, (18, 26, 32, 38)), (10, (14.4, 20.8, 25.6, 30.4)),
       (10, (892, 844, 808, 772))])),
    'HT4': TyrvingDataF('HT4', 'throw', *([0.12, 0.25, 0.5], [(18, (46, 48)),
       (18, (36.8, 38.4)), (18, (770, 760))])),
    'HT3': TyrvingDataF('HT3', 'throw', *([0.12, 0.25, 0.5],
       [(14, (34, 38, 41, 44)), (14, (27.2, 30.4, 32.8, 35.2)),
       (14, (830, 810, 795, 780))])),
    'HT2': TyrvingDataF('HT2', 'throw', *([0.12, 0.25, 0.5],
       [(10, (20, 27, 33, 38)), (10, (16, 21.6, 26.4, 30.4)),
       (10, (900, 865, 835, 810))])),
    'JT600': TyrvingDataF('JT600', 'throw', *([0.13, 0.25, 0.5],
       [(18, (42, 43)), (18, (33.6, 34.4)), (18, (790, 785))])),
    'JT500': TyrvingDataF('JT500', 'throw', *([0.13, 0.25, 0.5],
       [(15, (38, 40, 42)), (15, (30.4, 32, 33.6)), (15, (810, 800, 790))])),
    'JT400': TyrvingDataF('JT400', 'throw', *([0.13, 0.25, 0.5],
       [(10, (20, 27, 32, 36, 39)), (10, (16, 21.6, 25.6, 28.8, 31.2)),
       (10, (900, 865, 840, 820, 805))])),
    'OT150': TyrvingDataF('OT150', 'throw', *([0.1, 0.2, 0.4],
       [(10, (38, 43, 50, 56, 62)), (10, (30.4, 34.4, 40, 44.8, 49.6)),
       (10, (848, 828, 800, 776, 752))])),
    'BT1': TyrvingDataF('BT1', 'throw', *([0.13, 0.25, 0.5],
       [(10, (20, 26, 31)), (10, (16, 20.8, 24.8)), (10, (900, 865, 840))]))
  }
}

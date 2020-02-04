// automatically generated by ../../scripts/make-patterns-js.py

var FIELD_EVENTS = [
  'HJ',
  'SHJ',
  'PV',
  'LJ',
  'SLJ',
  'TJ',
  'STJ',
  'DT',
  'JT',
  'HT',
  'SP',
  'WT',
  'SWT',
  'BT',
  'ST',
  'GDT',
  'OT'
];
var FIELD_SORT_ORDER = [
  'HJ',
  'SHJ',
  'PV',
  'LJ',
  'SLJ',
  'TJ',
  'STJ',
  'SP',
  'DT',
  'HT',
  'JT',
  'ST',
  'GDT',
  'BT',
  'WT',
  'SWT',
  'OT'
];
var JUMPS = [
  'HJ',
  'SHJ',
  'PV',
  'LJ',
  'SLJ',
  'TJ',
  'STJ'
];
var MULTI_EVENTS = [
  'BI',
  'TRI',
  'QUAD',
  'PEN',
  'HEX',
  'HEP',
  'OCT',
  'ENN',
  'DEC',
  'HEN',
  'DOD',
  'ICO',
  'PENI',
  'PENWT',
  'MUL'
];
var STANDARD_FEMALE_TRACK_EVENTS = [
  '100',
  '200',
  '400',
  '800',
  '1500',
  '5000',
  '10000',
  '100H',
  '400H',
  '3000SC',
  '4x100',
  '4x400'
];
var STANDARD_MALE_TRACK_EVENTS = [
  '100',
  '200',
  '400',
  '800',
  '1500',
  '5000',
  '10000',
  '110H',
  '400H',
  '3000SC',
  '4x100',
  '4x400'
];
var THROWS = [
  'DT',
  'JT',
  'HT',
  'SP',
  'WT',
  'SWT',
  'BT',
  'ST',
  'GDT',
  'OT'
];
var PAT_EVENT_CODE = /^(?:[bB][iI]|[tT][rR][iI]|[qQ][uU][aA][dD]|[pP][eE][nN]|[hH][eE][xX]|[hH][eE][pP]|[oO][cC][tT]|[eE][nN][nN]|[dD][eE][cC]|[hH][eE][nN]|[dD][oO][dD]|[iI][cC][oO]|[pP][eE][nN][iI]|[pP][eE][nN][wW][tT])$|^(?:(?:(\d+)(?:[lLsS]?[hH](?:3[36])?|[yY]|[sS][cC]|[wW])?)|[sS][cC]|[2345][mM][tT]|[lL][hH]|[sS][hH])$|^(?:(?:[mM][iI][lL][eE]|[mM][aA][rR]|[hH][mM])[wW]?|[xX][cC]|(?:\d{1,3}(\.\d\d?)?(?:[MKk]|[MKk][wW]|[wW])))$|^(?:(?:[wW][tT](\d?\d\.?\d*[Kk]|)|[jJ][tT]([45678]00|)|[sS][wW][tT]|[gG][dD][tT]|[bB][tT](?:((?:\d|\d\.\d)[kK]))?|[oO][tT]|[dD][tT](\d\.?\d*[Kk]|)|[hH][tT](\d\.?\d*[Kk]|))|[sS][pP](\d\.?\d*[Kk]|))$|^(?:HJ|PV)$|^(?:LJ|TJ)$|^(?:(\d{1,2})[xX](\d{2,5}[hH]?|[rR][eE][lL][aA][yY]))$|^(?:(\d{2,4})([hH]|[sS][cC]))$|^(?:\d\d?([hH](?:[rR]|[wW])))$/;
var PAT_FIELD = /^(?:(?:[wW][tT](\d?\d\.?\d*[Kk]|)|[jJ][tT]([45678]00|)|[sS][wW][tT]|[gG][dD][tT]|[bB][tT](?:((?:\d|\d\.\d)[kK]))?|[oO][tT]|[dD][tT](\d\.?\d*[Kk]|)|[hH][tT](\d\.?\d*[Kk]|))|[sS][pP](\d\.?\d*[Kk]|))$|^(?:HJ|PV)$|^(?:LJ|TJ)$/;
var PAT_FINISH_RECORD = /^(\d{1,2}:)?(\d{1,2}:)?(\d{1,2})(\.?\d+)?$|^(DNF|DQ|DNS)$/;
var PAT_HORIZONTAL_JUMPS = /^(?:[sS]?[lL][jJ]|[sS]?[tT][jJ])$/;
var PAT_HURDLES = /^(?:(\d{2,4})([hH]|[sS][cC]))$/;
var PAT_JUMPS = /^(?:[sS]?[hH][jJ]|[pP][vV]|[sS]?[lL][jJ]|[sS]?[tT][jJ])$/;
var PAT_LEADING_DIGITS = /^\d+/;
var PAT_LEADING_FLOAT = /^\d+\.\d*/;
var PAT_LENGTH_EVENT = /^(?:LJ|TJ)$|^(?:(?:[wW][tT](\d?\d\.?\d*[Kk]|)|[jJ][tT]([45678]00|)|[sS][wW][tT]|[gG][dD][tT]|[bB][tT](?:((?:\d|\d\.\d)[kK]))?|[oO][tT]|[dD][tT](\d\.?\d*[Kk]|)|[hH][tT](\d\.?\d*[Kk]|))|[sS][pP](\d\.?\d*[Kk]|))$/;
var PAT_LONG_SECONDS = /^\d{3,6}(\.?\d+)?$/;
var PAT_MULTI = /^(?:[bB][iI]|[tT][rR][iI]|[qQ][uU][aA][dD]|[pP][eE][nN]|[hH][eE][xX]|[hH][eE][pP]|[oO][cC][tT]|[eE][nN][nN]|[dD][eE][cC]|[hH][eE][nN]|[dD][oO][dD]|[iI][cC][oO]|[pP][eE][nN][iI]|[pP][eE][nN][wW][tT])$/;
var PAT_NOT_FINISHED = /^(DNF|DQ|DNS)$/;
var PAT_PERF = /^(\d{1,2}:)?(\d{1,2}:)?(\d{1,2})(\.?\d+)?$/;
var PAT_RACES_FOR_DISTANCE = /^(?:\d\d?([hH](?:[rR]|[wW])))$/;
var PAT_RELAYS = /^(?:(\d{1,2})[xX](\d{2,5}[hH]?|[rR][eE][lL][aA][yY]))$/;
var PAT_ROAD = /^(?:(?:[mM][iI][lL][eE]|[mM][aA][rR]|[hH][mM])[wW]?|[xX][cC]|(?:\d{1,3}(\.\d\d?)?(?:[MKk]|[MKk][wW]|[wW])))$/;
var PAT_RUN = /^(?:(?:(\d+)(?:[lLsS]?[hH](?:3[36])?|[yY]|[sS][cC]|[wW])?)|[sS][cC]|[2345][mM][tT]|[lL][hH]|[sS][hH])$|^(?:(?:[mM][iI][lL][eE]|[mM][aA][rR]|[hH][mM])[wW]?|[xX][cC]|(?:\d{1,3}(\.\d\d?)?(?:[MKk]|[MKk][wW]|[wW])))$/;
var PAT_THROWS = /^(?:[dD][tT](\d?\.?\d*[Kk]|)|[jJ][tT]([45678]00|)|[hH][tT](\d?\.?\d*[Kk]|)|[sS][pP](\d?\.?\d*[Kk]|)|[wW][tT](\d?\.?\d*[Kk]|)|[sS][sW][tT](\d?\.?\d*[Kk]|)|[bB][tT](\d?\.?\d*[Kk]|)|[sS][tT](\d?\.?\d*[Kk]|)|[gG][dD][tT](\d?\.?\d*[Kk]|)|[oO][tT](\d?\.?\d*[Kk]|)|)$/;
var PAT_TIMED_EVENT = /^(?:(?:(\d+)(?:[lLsS]?[hH](?:3[36])?|[yY]|[sS][cC]|[wW])?)|[sS][cC]|[2345][mM][tT]|[lL][hH]|[sS][hH])$|^(?:(\d{2,4})([hH]|[sS][cC]))$|^(?:(?:[mM][iI][lL][eE]|[mM][aA][rR]|[hH][mM])[wW]?|[xX][cC]|(?:\d{1,3}(\.\d\d?)?(?:[MKk]|[MKk][wW]|[wW])))$|^(?:(\d{1,2})[xX](\d{2,5}[hH]?|[rR][eE][lL][aA][yY]))$/;
var PAT_TRACK = /^(?:(?:(\d+)(?:[lLsS]?[hH](?:3[36])?|[yY]|[sS][cC]|[wW])?)|[sS][cC]|[2345][mM][tT]|[lL][hH]|[sS][hH])$/;
var PAT_VERTICAL_JUMPS = /^(?:[sS]?[hH][jJ]|[pP][vV])$/;
var FIELD_EVENT_RECORDS_BY_GENDER = {
  all: {
    PV: 6.16,
    JT: 104.8,
    SP: 23.12,
    LJ: 8.95,
    HT: 86.74,
    HJ: 2.45,
    WT: 24.57,
    TJ: 18.29,
    DT: 76.8
  },
  m: {
    PV: 6.16,
    JT: 104.8,
    SP: 23.12,
    LJ: 8.95,
    HT: 86.74,
    HJ: 2.45,
    WT: 24.57,
    TJ: 18.29,
    DT: 74.08
  },
  f: {
    PV: 5.06,
    JT: 72.28,
    SP: 22.63,
    LJ: 7.52,
    HT: 82.98,
    HJ: 2.09,
    WT: 22.5,
    TJ: 15.5,
    DT: 76.8
  }
};

module.exports = {
  FIELD_EVENTS,
  FIELD_SORT_ORDER,
  JUMPS,
  MULTI_EVENTS,
  STANDARD_FEMALE_TRACK_EVENTS,
  STANDARD_MALE_TRACK_EVENTS,
  THROWS,
  PAT_EVENT_CODE,
  PAT_FIELD,
  PAT_FINISH_RECORD,
  PAT_HORIZONTAL_JUMPS,
  PAT_HURDLES,
  PAT_JUMPS,
  PAT_LEADING_DIGITS,
  PAT_LEADING_FLOAT,
  PAT_LENGTH_EVENT,
  PAT_LONG_SECONDS,
  PAT_MULTI,
  PAT_NOT_FINISHED,
  PAT_PERF,
  PAT_RACES_FOR_DISTANCE,
  PAT_RELAYS,
  PAT_ROAD,
  PAT_RUN,
  PAT_THROWS,
  PAT_TIMED_EVENT,
  PAT_TRACK,
  PAT_VERTICAL_JUMPS,
  FIELD_EVENT_RECORDS_BY_GENDER
};

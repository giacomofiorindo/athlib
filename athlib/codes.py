"""
Standard event codes, and things to parse and check them
Ensure all interesting lists and regexps are in the __all__
variable and no other objects are present.

All the exports should have capital letters.

>>> set(__all__) == set((_ for _ in globals().keys() if _.upper()==_))
True
"""
__all__ = (
        'FIELD_EVENTS', 'FIELD_SORT_ORDER', 'JUMPS', 'MULTI_EVENTS', 'STANDARD_FEMALE_TRACK_EVENTS',
        'STANDARD_MALE_TRACK_EVENTS', 'THROWS',
        'PAT_EVENT_CODE', 'PAT_FIELD', 'PAT_FINISH_RECORD', 'PAT_HORIZONTAL_JUMPS', 'PAT_HURDLES',
        'PAT_JUMPS', 'PAT_LEADING_DIGITS', 'PAT_LEADING_FLOAT', 'PAT_LENGTH_EVENT', 'PAT_LONG_SECONDS',
        'PAT_MULTI', 'PAT_NOT_FINISHED', 'PAT_PERF', 'PAT_RACES_FOR_DISTANCE', 'PAT_RELAYS', 'PAT_ROAD',
        'PAT_RUN', 'PAT_THROWS', 'PAT_TIMED_EVENT', 'PAT_TRACK', 'PAT_VERTICAL_JUMPS',
        )
import re
JUMPS = ("HJ", "PV", "LJ", "TJ")
THROWS = (
    "DT", "JT", "HT", "SP", "WT", 

    # Superweight Throw, Ball Throw, Other Throw, Stone Throw
    "SWT", "BT", "ST", "GDT", "OT"
)
MULTI_EVENTS = (
    # Greek prefixes for 2..12 events, and for 20.
    "BI", "TRI", "QUAD", "PEN", "HEX", "HEP", "OCT", "ENN", "DEC",
    "HEN", "DOD", "ICO",

    "PENI",  # Indoor Pentathlon, not sure if we should keep this
    "PENWT",  # Weights Pentathlon - defines what events go in it.
)
FIELD_EVENTS = JUMPS + THROWS
STANDARD_MALE_TRACK_EVENTS = ("100", "200", "400", "800", "1500",
                              "5000", "10000",
                              "110H", "400H", "3000SC", "4x100", "4x400")
STANDARD_FEMALE_TRACK_EVENTS = tuple(("100H" if x == "110H" else
                                x for x in STANDARD_MALE_TRACK_EVENTS))
# When listing field events, the Blazer Brigade suggest this should be the
# order
FIELD_SORT_ORDER = ["HJ", "PV", "LJ", "TJ", "SP", "DT", "HT", "JT", 
  "ST", "GDT", "BT", "WT", "SWT", "OT"]


# Patterns allow both for generic (JT = Javelin Throw) and
# weight-specific (JT800) patterns.
_ = r"\d\.?\d*[Kk]"
PAT_THROWS = re.compile((r"^(?:(?:[wW][tT](?P<wtnum>\d?%s|)|[jJ][tT](?P<jtnum>[45678]00|)|"
    r"[sS][wW][tT]|[gG][dD][tT]|[bB][tT](?:(?P<btnum>(?:\d|\d\.\d)[kK]))?|[oO][tT]|"
                         r"[dD][tT](?P<dtnum>%s|)|[hH][tT](?P<htnum>%s|))|"
                         r"[sS][pP](?P<spnum>%s|))$") % (_, _, _, _),
                        )
PAT_VERTICAL_JUMPS = re.compile(r"^(?:HJ|PV)$")
PAT_HORIZONTAL_JUMPS = re.compile(r"^(?:LJ|TJ)$")
PAT_JUMPS = re.compile("|".join(_.pattern for _ in (PAT_VERTICAL_JUMPS,PAT_HORIZONTAL_JUMPS)))
PAT_TRACK = re.compile(r"^(?:(?:(?P<meters>\d+)(?:[lLsS]?[hH](?:3[36])?|[yY]|[sS][cC]|[wW])?)|[sS][cC]|"
                        r"[2345][mM][tT]|[lL][hH]|[sS][hH])$",
                       )
PAT_ROAD = re.compile(r"^(?:(?:[mM][iI][lL][eE]|[mM][aA][rR]|[hH][mM])[wW]?|[xX][cC]|(?:\d{1,3}(\.\d\d?)?(?:[MKk]|[MKk][wW]|[wW])))$")

PAT_RACES_FOR_DISTANCE = re.compile(r"^(?:\d\d?([hH](?:[rR]|[wW])))$")

PAT_RUN = re.compile("%s|%s" % (PAT_TRACK.pattern, PAT_ROAD.pattern))
PAT_FIELD = re.compile("%s|%s" % (PAT_THROWS.pattern, PAT_JUMPS.pattern))

# Although part of PAT_RUN, these
PAT_RELAYS = re.compile("^(?:(\d{1,2})[xX](\d{2,5}[hH]?|[rR][eE][lL][aA][yY]))$") # 4x100, 4x400, 4xReLAy, 12x200H
PAT_HURDLES = re.compile("^(?:(\d{2,4})([hH]|[sS][cC]))$") # 80H, 110H, 400H
PAT_MULTI = '|'.join((''.join(('[%s%s]' % (v.lower(),v.upper()) for v in _)) for _ in MULTI_EVENTS))
PAT_MULTI = re.compile(r"^(?:%s)$" % PAT_MULTI)
PAT_EVENT_CODE=re.compile('|'.join(_.pattern for _ in (PAT_MULTI,PAT_RUN,
                PAT_FIELD,PAT_RELAYS,PAT_HURDLES,PAT_RACES_FOR_DISTANCE)))

PAT_LEADING_FLOAT = re.compile(r"^\d+\.\d*")
PAT_LEADING_DIGITS = re.compile("^\d+")

PAT_LENGTH_EVENT = re.compile("|".join(_.pattern for _ in (PAT_HORIZONTAL_JUMPS, PAT_THROWS)))
PAT_TIMED_EVENT = re.compile("|".join(_.pattern for _ in (PAT_TRACK, PAT_HURDLES, PAT_ROAD, PAT_RELAYS)))

# matches optional hours, optional minutes, optional seconds, optional two decimal places
PAT_PERF = re.compile("^(\d{1,2}:)?(\d{1,2}:)?(\d{1,2})(\.?\d+)?$")

# matches time pasted as seconds only, more than 100 sec.
PAT_LONG_SECONDS = re.compile(u"^\d{3,6}(\.?\d+)?$")

PAT_NOT_FINISHED =  re.compile(r"^(DNF|DQ|DNS)$")

# these are the values one might get in results - valid time, DNF, DQ etc.
PAT_FINISH_RECORD = re.compile("|".join(_.pattern for _ in (PAT_PERF, PAT_NOT_FINISHED)))
del _

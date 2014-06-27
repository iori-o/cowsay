#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import textwrap

def savanna():
  return u"""

  　ノ从从从从ヽ
  (⌒／ﾞﾞﾞﾞﾞﾞﾞﾞ＼⌒)
　ノｲ ＿　　＿ ｜ヽ
　彡|ヽ･〉〈･ﾉ ｜ミ
　彡|　　▼　　 ｜ミ
　彡ヽ ＿人＿  / ミ
`／ヾヽ `⌒′/ ツ＼
｜　ヾ ﾞﾞﾞﾞﾞﾞ ツ｜
｜　| ヾ从从
  """

def say(serif, length=40):
  return build_balloon(serif, length) + savanna()

def build_balloon(serif, length=40):
    balloon    = []
    lines      = normalize_text(serif, length)

    bordersize = calculate_bordersize(lines[0])

    balloon.append(" " + "_" * bordersize)

    for index, line in enumerate(lines):
        border = get_border(lines, index)
        balloon.append(u"%s %s %s" % (border[0], line, border[1]))

    balloon.append(" " + "-" * bordersize)

    return "\n".join(balloon)

def calculate_bordersize(line):
  return len(line * 2) if isinstance(line, unicode) else len(line)

def normalize_text(str, length):
    lines  = textwrap.wrap(str, length)
    maxlen = len(max(lines, key=len))

    return [ line.ljust(maxlen) for line in lines ]

def get_border(lines, index):
    if len(lines) < 2:
        return [ "<", ">" ]
    elif index == 0:
        return [ "/", "\\" ]
    elif index == len(lines) - 1:
        return [ "\\", "/" ]
    else:
        return [ "|", "|" ]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: '%s string'" % sys.argv[0]
        sys.exit(0)

    serif = unicode(sys.argv[1], "utf-8")
    print say(serif)

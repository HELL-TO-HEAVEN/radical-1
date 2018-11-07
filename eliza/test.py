#!/usr/bin/env python      
# -*- coding: utf-8 -*-     
# Author: feng
from utilities import cut
from eliza.pattern_match import pattern_match_l, segment_match, defaultdict

# pattern=tuple(cut('?*xAI?*y'))
# speech='hello'
pattern=tuple(cut('?*x hello ?*y'))
speech='hello'
print(pattern_match_l(list(pattern), speech))

bindings = None or defaultdict(lambda : None)
input = speech
segment_match(pattern, input, bindings)

# 0, get_rule function changed
# 1, pattern  =>  complete split this pattern?
# 2, first_match_pos function chang?


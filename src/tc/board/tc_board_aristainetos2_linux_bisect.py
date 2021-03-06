# This file is part of tbot.  tbot is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Description:
# start with
# tbot.py -s lab_denx -c aristainetos2 -t tc_board_aristainetos2_linux_bisect.py
# start a git bisect for the aristainetos2 board
# End:
#
from tbotlib import tbot

tb.config.board_git_bisect_get_source_tc = "tc_workfd_goto_linux_code.py"
tb.config.board_git_bisect_call_tc = "tc_board_aristainetos2_linux_tests.py"
tb.config.board_git_bisect_good_commit = "da9373d67c8a7adf7d820f24fe672c5540f231ac"
tb.config.board_git_bisect_patches = tb.config.tc_lab_apply_patches_dir

tb.eof_call_tc("tc_board_git_bisect.py")

tb.end_tc(True)

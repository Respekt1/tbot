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
# python2.7 src/common/tbot.py -c tbot_board.cfg -t tc_demo_can_part1.py
# start tc:
# starts a can demo
# For this demo the fipad board in the denx lab is used.
# To test the CAN bus we have in the DENX lab installed a PC, called
# CANPC to which a PEAK CAN adapter is attached, which then is connected
# to the CAN bus the fipad board is also connected.
#
# We use tc_workfd_can.py for testing
#
# We open a new connection to the LabPC, called canm and then we ssh
# to the CANPC, from where we then start candump, while on the console
# connection a cansend was started. So we can read from the canm
# connection, the bytes we send with cansend on the console connection.
#
# If we got the same bytes as we send -> TC True
# else the TC returns False
#
# Only one cansend call is tested ... room for more.
# End:

from tbotlib import tbot

# set board into state linux
tb.set_board_state("linux")

# start the can test
tb.eof_call_tc("tc_workfd_can.py")
tb.end_tc(True)

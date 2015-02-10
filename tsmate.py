#!/usr/bin/python

from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from subprocess import PIPE
import subprocess
import sys
from pymediainfo import MediaInfo
import pyqtgraph.parametertree.parameterTypes as pTypes
from pyqtgraph.parametertree import Parameter, ParameterTree, ParameterItem, registerParameterType
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)



goporder = 1;
#Get the file
input = sys.argv[1]



print "Please wait, parsing media."
#Get mediainfo about the file
params = [
    {'name': 'Filename', 'type': 'str', 'value': input, 'siPrefix': False, 'suffix': '', 'readonly': True},
    {'name': 'General', 'type': 'group', 'children': [
    ]},
    {'name': 'Video', 'type': 'group', 'children': [
    ]},
    {'name': 'Audio', 'type': 'group', 'children': [
    ]}
]

audiopid = -1;
videopid = -1;

exceptions = []
exceptions.append("Test start")

media_info = MediaInfo.parse(input)
try:
    for track in media_info.tracks:
        if track.track_type == 'General':
            bitrate =  track.overall_bit_rate
            params[1]['children'].append({'name': "File Extention", 'type': 'str', 'value':track.file_extension, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[1]['children'].append({'name': "File Size", 'type': 'str', 'value':track.file_size, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[1]['children'].append({'name': "Duration", 'type': 'str', 'value':track.duration, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[1]['children'].append({'name': "Bitrate Mode", 'type': 'str', 'value':track.overall_bit_rate_mode, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[1]['children'].append({'name': "Bitrate", 'type': 'str', 'value':track.overall_bit_rate, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[1]['children'].append({'name': "Delay", 'type': 'str', 'value':track.delay, 'siPrefix': False, 'suffix': '', 'readonly': True})
        if track.track_type == 'Video':
            params[2]['children'].append({'name': "PID", 'type': 'str', 'value':track.track_id, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[2]['children'].append({'name': "Format", 'type': 'str', 'value':track.format, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[2]['children'].append({'name': "Format_Profile", 'type': 'str', 'value':track.format_profile, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[2]['children'].append({'name': "Format_Settings", 'type': 'str', 'value':track.format_settings, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[2]['children'].append({'name': "Codec_Profile", 'type': 'str', 'value':track.codec_profile, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[2]['children'].append({'name': "Duration", 'type': 'str', 'value':track.duration, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[2]['children'].append({'name': "Bitrate Mode", 'type': 'str', 'value':track.bit_rate_mode, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[2]['children'].append({'name': "Bitrate", 'type': 'str', 'value':track.bit_rate, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[2]['children'].append({'name': "BufferSize", 'type': 'str', 'value':track.buffer_size, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[2]['children'].append({'name': "Width", 'type': 'str', 'value':track.width, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[2]['children'].append({'name': "Height", 'type': 'str', 'value':track.height, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[2]['children'].append({'name': "PixelAspectRatio", 'type': 'str', 'value':track.pixel_aspect_ratio, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[2]['children'].append({'name': "DisplayAspectRatio", 'type': 'str', 'value':track.display_aspect_ratio, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[2]['children'].append({'name': "FrameRate", 'type': 'str', 'value':track.frame_rate, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[2]['children'].append({'name': "FrameCount", 'type': 'str', 'value':track.frame_count, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[2]['children'].append({'name': "Standard", 'type': 'str', 'value':track.standard, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[2]['children'].append({'name': "BitDepth", 'type': 'str', 'value':track.bit_depth, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[2]['children'].append({'name': "ScanType", 'type': 'str', 'value':track.scan_type, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[2]['children'].append({'name': "ScanOrder", 'type': 'str', 'value':track.scan_order, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[2]['children'].append({'name': "Delay", 'type': 'str', 'value':track.delay, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[2]['children'].append({'name': "StreamSize", 'type': 'str', 'value':track.stream_size, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[2]['children'].append({'name': "Language", 'type': 'str', 'value':track.language, 'siPrefix': False, 'suffix': '', 'readonly': True})
        if track.track_type == 'Audio':
            params[3]['children'].append({'name': "PID", 'type': 'str', 'value':track.track_id, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[3]['children'].append({'name': "Format", 'type': 'str', 'value':track.format, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[3]['children'].append({'name': "Duration", 'type': 'str', 'value':track.duration, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[3]['children'].append({'name': "Bitrate Mode", 'type': 'str', 'value':track.bit_rate_mode, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[3]['children'].append({'name': "Bitrate", 'type': 'str', 'value':track.bit_rate, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[3]['children'].append({'name': "Channels", 'type': 'str', 'value':track.channel_count, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[3]['children'].append({'name': "Sample Rate", 'type': 'str', 'value':track.sampling_rate, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[3]['children'].append({'name': "BitDepth", 'type': 'str', 'value':track.bit_depth, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[3]['children'].append({'name': "Delay", 'type': 'str', 'value':track.delay, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[3]['children'].append({'name': "StreamSize", 'type': 'str', 'value':track.stream_size, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[3]['children'].append({'name': "Dial Norm Avg", 'type': 'str', 'value':track.dialnorm_average, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[3]['children'].append({'name': "Dial Norm Min", 'type': 'str', 'value':track.dialnorm_minimum, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[3]['children'].append({'name': "Dial Norm Max", 'type': 'str', 'value':track.dialnorm_maximum, 'siPrefix': False, 'suffix': '', 'readonly': True})
            params[3]['children'].append({'name': "Language", 'type': 'str', 'value':track.language, 'siPrefix': False, 'suffix': '', 'readonly': True})
except:
    print "Unable to parse the file with mediainfo\n"
    sys.exit(0)

#
# PCR AND PMT PIDS
#
#Todo one command and python find
pmtpid  = subprocess.check_output("/usr/bin/tsinfo " + input + " 2>&1 |grep \"PMT with\" |awk '{print $8}' | sed 's/[()]//g'", shell=True)
pcrpid = subprocess.check_output("/usr/bin/tsinfo " + input + " 2>&1 |grep \"PCR\" |awk '{print $8}' | sed 's/[()]//g'", shell=True)
audiopid  = subprocess.check_output("/usr/bin/tsinfo " + input + " 2>&1 |grep \"User private\" |awk '{print $4}' | sed 's/[()]//g'", shell=True)
videopid = subprocess.check_output("/usr/bin/tsinfo " + input + " 2>&1 |grep \"video\" |awk '{print $4}' | sed 's/[()]//g'", shell=True)


#LEVEL 1
ETR_290_TS_SYNC_LOSS_COUNT = 0
ETR_290_SYNC_BYTE_ERROR_COUNT = 0
ETR_290_PAT_DELTA_ERROR_COUNT = 0
ETR_290_PAT_TABLE_ERROR_COUNT = 0
ETR_290_PAT_SC_ERROR_COUNT = 0
ETR_290_CC_ERROR_COUNT = 0
ETR_290_PMT_DELTA_ERROR_COUNT = 0
ETR_290_PMT_TABLE_ERROR_COUNT = 0
ETR_290_PMT_SC_ERROR_COUNT = 0
ETR_290_PID_ERROR_COUNT = 0

#LEVEL 2
ETR_290_TRANSPORT_ERROR_COUNT = 0
ETR_290_CRC_ERROR_COUNT = 0
ETR_290_PCR_DELTA100_ERROR_COUNT = 0
ETR_290_PCR_DELTA40_ERROR_COUNT = 0
ETR_290_PCR_ACCURACY_ERROR_COUNT = 0
ETR_290_PTS_DELTA_ERROR_COUNT = 0
ETR_290_CAT_SC_COUNT = 0
ETR_290_CAT_TABLE_ERROR_COUNT = 0

ETR_290_NIT_DELTA_ERROR_COUNT = 0
ETR_290_NIT_TABLE_ERROR_COUNT = 0
ETR_290_SI_REP_ERROR_COUNT = 0
ETR_290_BUFFER_ERROR_COUNT = 0
ETR_290_OTHERPID_ERROR_COUNT = 0
ETR_290_SDT_NA_ERROR_COUNT = 0
ETR_290_SDT_TABLE_ERROR_COUNT = 0
ETR_290_SDT_NA_ERROR_COUNT = 0
ETR_290_EIT_NA_ERROR_COUNT = 0
ETR_290_EIT_TABLE_ERROR_COUNT = 0
ETR_290_RST_ERROR_COUNT = 0
ETR_290_TDT_NA_ERROR_COUNT = 0
ETR_290_TDT_TABLE_ERROR_COUNT = 0
ETR_290_EMPTY_BUFFER_ERROR_COUNT = 0
ETR_290_DATA_DELAY_ERROR_COUNT = 0

output = subprocess.check_output("/usr/local/bin/tsetr290 " + input + " " + str(bitrate) + " 1 " , shell=True) 
etr_info = map(str, output.split("\n"))



for x in etr_info:
    if(x.find("ERROR")):
        if(x.find("1.1") > 0):
            print x
            ETR_290_TS_SYNC_LOSS_COUNT+=1
        elif(x.find("1.2") > -1):
            ETR_290_SYNC_BYTE_ERROR_COUNT+=1
        elif(x.find("1.3a") > -1):
            ETR_290_PAT_DELTA_ERROR_COUNT+=1
        elif(x.find("1.3b") > -1):
            ETR_290_PAT_TABLE_ERROR_COUNT+=1
        elif(x.find("1.3c") > -1):
            ETR_290_PAT_SC_ERROR_COUNT+=1
            exceptions.append(x)
        elif(x.find("1.4") > -1):
            ETR_290_CC_ERROR_COUNT+=1
        elif(x.find("1.5a") > -1):
            ETR_290_PMT_DELTA_ERROR_COUNT+=1
        elif(x.find("1.5b") > -1):
            ETR_290_PMT_TABLE_ERROR_COUNT+=1
        elif(x.find("1.5c") > -1):
            ETR_290_PMT_SC_ERROR_COUNT+=1
        elif(x.find("1.6") > -1):
            ETR_290_PID_ERROR_COUNT+=1
        elif(x.find("2.1") > -1):
            ETR_290_TRANSPORT_ERROR_COUNT+=1
        elif(x.find("2.2") > -1):
            ETR_290_CRC_ERROR_COUNT+=1
        elif(x.find("2.3a") > -1):
            ETR_290_PCR_DELTA100_ERROR_COUNT+=1
        elif(x.find("2.3b") > -1):
            ETR_290_PCR_DELTA40_ERROR_COUNT+=1
        elif(x.find("2.4") > -1):
            ETR_290_PCR_ACCURACY_ERROR_COUNT+=1
        elif(x.find("2.5") > -1):
            ETR_290_PTS_DELTA_ERROR_COUNT+=1
        elif(x.find("2.6a") > -1):
            ETR_290_CAT_SC_COUNT+=1
        elif(x.find("2.6b") > -1):
            ETR_290_CAT_TABLE_ERROR_COUNT+=1
        elif(x.find("3.1a") > -1):
            ETR_290_NIT_DELTA_ERROR_COUNT+=1
        elif(x.find("3.1b") > -1):
            ETR_290_NIT_TABLE_ERROR_COUNT+=1
        elif(x.find("3.2") > -1):
            ETR_290_SI_REP_ERROR_COUNT+=1
        elif(x.find("3.3") > -1):
            ETR_290_BUFFER_ERROR_COUNT+=1
        elif(x.find("3.4") > -1):
            ETR_290_OTHERPID_ERROR_COUNT+=1
        elif(x.find("3.5a") > -1):
            ETR_290_SDT_NA_ERROR_COUNT+=1
        elif(x.find("3.5b") > -1):
            ETR_290_SDT_TABLE_ERROR_COUNT+=1
        elif(x.find("3.6a") > -1):
            ETR_290_EIT_NA_ERROR_COUNT+=1
        elif(x.find("3.6b") > -1):
            ETR_290_EIT_TABLE_ERROR_COUNT+=1
        elif(x.find("3.7") > -1):
            ETR_290_RST_ERROR_COUNT+=1
        elif(x.find('3.8a') > -1):
            ETR_290_TDT_NA_ERROR_COUNT+=1
        elif(x.find("3.8b") > -1):
            ETR_290_TDT_TABLE_ERROR_COUNT+=1		
        elif(x.find("3.9") > -1):
            ETR_290_EMPTY_BUFFER_ERROR_COUNT+=1
        elif(x.find("3.10") > -1):
            ETR_290_DATA_DELAY_ERROR_COUNT+=1
        exceptions.append(x)
#print exceptions
#exit(0)
etrparams = [
    {'name': 'Priority 1.', 'type': 'group', 'children': [
        {'name': "1.1  TS Sync Loss", 'type': 'str', 'value':str(ETR_290_TS_SYNC_LOSS_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "1.2  Sync Byte Error", 'type': 'str', 'value':str(ETR_290_SYNC_BYTE_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "1.3a PAT Table Error", 'type': 'str', 'value':str(ETR_290_PAT_DELTA_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "1.3b PAT delta Error", 'type': 'str', 'value':str(ETR_290_PAT_TABLE_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "1.3c PAT Scrambling Control Error", 'type': 'str', 'value':str(ETR_290_PAT_SC_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "1.4  Continuity Count Error", 'type': 'str', 'value':str(ETR_290_CC_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "1.5a PMT Delta Error", 'type': 'str', 'value':str(ETR_290_PMT_DELTA_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "1.5b PMT Table Error", 'type': 'str', 'value':str(ETR_290_PMT_TABLE_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "1.5c PMT Scrambling Control Error", 'type': 'str', 'value':str(ETR_290_PMT_SC_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "1.6  PID Error", 'type': 'str', 'value':str(ETR_290_PID_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True}
    ]},
    {'name': 'Priority 2.', 'type': 'group', 'children': [
        {'name': "2.1  Transport Error", 'type': 'str', 'value':str(ETR_290_TRANSPORT_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "2.2  CRC Error", 'type': 'str', 'value':str(ETR_290_CRC_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "2.3a PCR_Delta 100 Error", 'type': 'str', 'value': str(ETR_290_PCR_DELTA100_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "2.3b PCR_Delta 40 Error", 'type': 'str', 'value':str(ETR_290_PCR_DELTA40_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "2.4  PCR Accuracy Error", 'type': 'str', 'value':str(ETR_290_PCR_ACCURACY_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "2.5  PTS_error", 'type': 'str', 'value':str(ETR_290_PTS_DELTA_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "2.6a CAT Scrambling Control Error", 'type': 'str', 'value':str(ETR_290_CAT_SC_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "2.6b CAT Table Error", 'type': 'str', 'value':str(ETR_290_CAT_TABLE_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True} 
    ]},
    {'name': 'Priority 3.', 'type': 'group', 'children': [
        {'name': "3.1a NIT Delta Error", 'type': 'str', 'value':str(ETR_290_NIT_DELTA_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "3.1b NIT Table Error", 'type': 'str', 'value':str(ETR_290_NIT_TABLE_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "3.2  SI Delta Error", 'type': 'str', 'value':str(ETR_290_SI_REP_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "3.3  Buffer Error", 'type': 'str', 'value':str(ETR_290_BUFFER_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "3.4  Unreference_PID", 'type': 'str', 'value':str(ETR_290_OTHERPID_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "3.5a SDT Delta Error", 'type': 'str', 'value':str(ETR_290_SDT_NA_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "3.5b SDT Table Error", 'type': 'str', 'value':str(ETR_290_SDT_TABLE_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "3.6a EIT Delta Error", 'type': 'str', 'value':str(ETR_290_EIT_NA_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "3.6b EIT Table Error", 'type': 'str', 'value':str(ETR_290_EIT_TABLE_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "3.7  RST Error", 'type': 'str', 'value':str(ETR_290_RST_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "3.8a TDT Delta Error", 'type': 'str', 'value':str(ETR_290_TDT_NA_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "3.8b TDT Table Error", 'type': 'str', 'value':str(ETR_290_TDT_TABLE_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "3.9  Empty Buffer Error", 'type': 'str', 'value':str(ETR_290_EMPTY_BUFFER_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True},
        {'name': "3.10 Data Delay Error", 'type': 'str', 'value':str(ETR_290_DATA_DELAY_ERROR_COUNT), 'siPrefix': False, 'suffix': '', 'readonly': True}
    ]}
]

pmt = []
pat = []
pcrd = []
pcrj = []
sdt = []
eit = []
nit = []
tdt = []

try:
    for line in open(input + '.pmt_delta_report.csv'):
        nums = line.split()
        nums = map(float, nums)
        pmt.extend(nums)
except:
    print "Unable to fetch pmt csv\n"

try: 
    for line in open(input + '.pat_delta_report.csv'):
        nums = line.split()
        nums = map(float, nums)
        pat.extend(nums)
except:
    print "Unable to fetch pat csv\n"
try:
    for line in open(input + '.pcr_delta_report.csv'):
        nums = line.split()
        nums = map(float, nums)
        pcrd.extend(nums)
except:
    print "Unable to fetch pcr delta csv\n"
try:
    for line in open(input + '.pcr_jitter_report.csv'):
        nums = line.split()
        nums = map(float, nums)
        pcrj.extend(nums)
except:
    print "Unable to fetch pcr jitter csv\n"
try:
    for line in open(input + '.eit_delta_report.csv'):
        nums = line.split()
        nums = map(float, nums)
        eit.extend(nums)
except:
    print "Unable to fetch eit csv\n"
try:
    for line in open(input + '.sdt_delta_report.csv'):
        nums = line.split()
        nums = map(float, nums)
        sdt.extend(nums)
except:
    print "Unable to fetch sdt csv\n"
try:
    for line in open(input + '.nit_delta_report.csv'):
        nums = line.split()
        nums = map(float, nums)
        nit.extend(nums)
except:
    print "Unable to fetch nit csv\n"
try:
    for line in open(input + '.tdt_delta_report.csv'):
        nums = line.split()
        nums = map(float, nums)
        tdt.extend(nums)
except:
    print "Unable to fetch tdt csv\n"






exceptions.append("Test End")


output = subprocess.check_output("/usr/local/bin/ffprobe -show_frames " + input + " 2>&1"  , shell=True) 
frame_info = map(str, output.split("\n"))

cpn = []
dpn = []
pictypes = [] 
frame = 0
for x in frame_info:
    if(x.find("pict_type")>-1):
        type = x.split("=")
        pictypes.append(type[1])
    if(x.find("coded_picture_number")>-1):
        type = x.split("=")
        cpn.append(type[1])
    if(x.find("display_picture_number")>-1):
        type = x.split("=")
        dpn.append(type[1])
app = QtGui.QApplication([])


## Create tree of Parameter objects
p = Parameter.create(name='params', type='group', children=params)

etrparams = Parameter.create(name='etrparams', type='group', children=etrparams)

t = ParameterTree()
t.setParameters(p, showTop=False)

etr = ParameterTree()
etr.setParameters(etrparams, showTop=False)

pg.setConfigOptions(antialias=True)

win = QtGui.QWidget()
layout = QtGui.QGridLayout()
pcr_timing = QtGui.QGridLayout()

pat_panel = QtGui.QGridLayout()
pmt_panel = QtGui.QGridLayout()
sdt_panel = QtGui.QGridLayout()
nit_panel = QtGui.QGridLayout()
eit_panel = QtGui.QGridLayout()
tdt_panel = QtGui.QGridLayout()
frame_panel = QtGui.QGridLayout()



mediainfo = QtGui.QVBoxLayout()
log	= QtGui.QVBoxLayout()
framelog	= QtGui.QVBoxLayout()
etr290 = QtGui.QVBoxLayout()
tabs	= QtGui.QTabWidget()


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

framerlog = QtGui.QListWidget()
framerlog.setViewMode(QtGui.QListView.IconMode)
framerlog.setIconSize(QtCore.QSize(24, 24))
framerlog.setSpacing(3)

icon1 = QtGui.QIcon("icons/I.png")
iframe = icon1.pixmap(24, 24, QtGui.QIcon.Normal, QtGui.QIcon.On)
icon2 = QtGui.QIcon("icons/B.png")
bframe = icon2.pixmap(24, 24, QtGui.QIcon.Normal, QtGui.QIcon.On)
icon3 = QtGui.QIcon("icons/P.png")
pframe = icon3.pixmap(24, 24, QtGui.QIcon.Normal, QtGui.QIcon.On)
icon4 = QtGui.QIcon("icons/list.png")
pframe = icon4.pixmap(24, 24, QtGui.QIcon.Normal, QtGui.QIcon.On)


gopmenu = QtGui.QToolBar()
ordertype  = gopmenu.addAction(icon4, '&Decode/Display Order')
ordertype_label  = QtGui.QLabel(' Display Order')
gopmenu.addWidget(ordertype_label)



do = []
def change_gop_order():
	global goporder, pictypes, cpn,ordertype_label
	if(goporder == 1):
		ordertype_label.setText(" Display Order")
		goporder =0
	else:
		ordertype_label.setText(" Decode Order")
		goporder =1
	do = []
	framerlog.clear()
	if(goporder ==0):
	    #Recode in display order from coded order
	    i=0
	    for x in cpn:
	    	n = pictypes[int(i)]
	    	do.insert(int(x), n)
	    	i+=1
	    i=0
	else:
		do = pictypes
	for x in do:
		item = QtGui.QListWidgetItem(x)
		if(x == "I"):
			item.setIcon(icon1)
			item.setBackground(QtGui.QColor('#A84F00'))
			item.setForeground(QtGui.QColor('white'))
		elif(x == "B"):
			item.setIcon(icon2)
			item.setBackground(QtGui.QColor('#015E66'))
			item.setForeground(QtGui.QColor('white'))
		elif(x =="P"):
			item.setIcon(icon3)
			item.setBackground(QtGui.QColor('#008310'))
			item.setForeground(QtGui.QColor('white'))
		framerlog.addItem(item)

		
change_gop_order()

ordertype.setStatusTip('Re-order Gop between coded and display order')
ordertype.triggered.connect(change_gop_order)


tab1 = QtGui.QWidget()	
tab2 = QtGui.QWidget()
tab3 = QtGui.QWidget()
tab4 = QtGui.QWidget()
tab5 = QtGui.QWidget()
tab6 = QtGui.QWidget()
tab7 = QtGui.QWidget()
tab8 = QtGui.QWidget()
tab9 = QtGui.QWidget()
tab10 = QtGui.QWidget()
tab11 = QtGui.QWidget()

tabs.addTab(tab1,"MediaInfo")
tabs.addTab(tab3,"Error Log")
tabs.addTab(tab4,"ETR 290 Report")
if(len(pcrd) > 0 or len(pcrj) > 0):
    tabs.addTab(tab2,"PCR Timing")
if(len(pat) > 0):
    tabs.addTab(tab5,"PAT")
if(len(pmt) > 0):
    tabs.addTab(tab6,"PMT")
if(len(sdt) > 0):
    tabs.addTab(tab7,"SDT")
if(len(nit) > 0):
    tabs.addTab(tab8,"NIT")
if(len(eit) > 0):
    tabs.addTab(tab9,"EIT")
if(len(tdt) > 0):
    tabs.addTab(tab10,"TDT")
if(len(pictypes) > 0):
    tabs.addTab(tab11,"GOP")

win.setLayout(layout)
if(len(pcrd) > 0):
    w1 = pg.PlotWidget(title="PCR Interval (ms)")
    w1.plot(pcrd,pen=(0,255,0))
    pcr_timing.addWidget(w1)
if(len(pcrj) > 0):
    w1 = pg.PlotWidget(title="PCR Jitter (ms)")
    w1.plot(pcrj,pen=(0,0,255))
    pcr_timing.addWidget(w1)
if(len(pat) > 0):
    w3 = pg.PlotWidget(title="PAT Interval (ms)")
    w3.plot(pat,pen=(0,255,255))
    pat_panel.addWidget(w3)
if(len(pmt) > 0):
    w2 = pg.PlotWidget(title="PMT Interval (ms)")
    w2.plot(pmt,pen=(255,255,0))
    pmt_panel.addWidget(w2)
if(len(sdt) > 0):
    w3 = pg.PlotWidget(title="SDT Interval (ms)")
    w3.plot(sdt,pen=(255,255,255))
    sdt_panel.addWidget(w3)
if(len(nit) > 0):
    w3 = pg.PlotWidget(title="NIT Interval (ms)")
    w3.plot(nit,pen=(255,255,255))
    nit_panel.addWidget(w3)
if(len(eit) > 0):
    w3 = pg.PlotWidget(title="EIT Interval (ms)")
    w3.plot(eit,pen=(255,255,255))
    eit_panel.addWidget(w3)
if(len(tdt) > 0):
    w3 = pg.PlotWidget(title="TDT Interval (ms)")
    w3.plot(tdt,pen=(255,255,255))
    tdt_panel.addWidget(w3)
if(len(pictypes) > 0):
    frame_panel.addWidget(gopmenu)
    frame_panel.addWidget(framerlog)


errorlog = QtGui.QPlainTextEdit()
for x in exceptions:
    errorlog.insertPlainText(x + "\n")
    
log.addWidget(errorlog)
mediainfo.addWidget(t)
etr290.addWidget(etr)

tab1.setLayout(mediainfo)
if(len(pcrd) > 0 or len(pcrj) > 0):
    tab2.setLayout(pcr_timing)
tab3.setLayout(log)
tab4.setLayout(etr290)
if(len(pat) > 0):
    tab5.setLayout(pat_panel)
if(len(pmt) > 0):
    tab6.setLayout(pmt_panel)
if(len(sdt) > 0):
    tab7.setLayout(sdt_panel)
if(len(nit) > 0):
    tab8.setLayout(nit_panel)
if(len(eit) > 0):
    tab9.setLayout(eit_panel)
if(len(tdt) > 0):
    tab10.setLayout(tdt_panel)    
if(len(pictypes) > 0):
    tab11.setLayout(frame_panel)    
    
    
layout.addWidget(tabs, 2, 0, 1, 1)
win.show()
## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
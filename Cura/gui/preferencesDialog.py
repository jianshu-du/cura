from __future__ import absolute_import

import wx

from Cura.gui import configBase
from Cura.util import validators
from Cura.util import machineCom
from Cura.util import profile

class preferencesDialog(wx.Frame):
	def __init__(self, parent):
		super(preferencesDialog, self).__init__(None, title="Preferences", style=wx.DEFAULT_DIALOG_STYLE)
		
		wx.EVT_CLOSE(self, self.OnClose)
		
		self.parent = parent
		self.oldExtruderAmount = int(profile.getPreference('extruder_amount'))

		self.panel = configBase.configPanelBase(self)
		
		left, right, main = self.panel.CreateConfigPanel(self)
		configBase.TitleRow(left, 'Machine settings')
		configBase.SettingRow(left, 'steps_per_e')
		configBase.SettingRow(left, 'machine_width')
		configBase.SettingRow(left, 'machine_depth')
		configBase.SettingRow(left, 'machine_height')
		configBase.SettingRow(left, 'extruder_amount')
		configBase.SettingRow(left, 'has_heated_bed')
		
		for i in xrange(1, self.oldExtruderAmount):
			configBase.TitleRow(left, 'Extruder %d' % (i+1))
			configBase.SettingRow(left, 'extruder_offset_x%d' % (i))
			configBase.SettingRow(left, 'extruder_offset_y%d' % (i))

		configBase.TitleRow(left, 'Colours')
		configBase.SettingRow(left, 'model_colour')
		for i in xrange(1, self.oldExtruderAmount):
			configBase.SettingRow(left, 'model_colour%d' % (i+1))

		configBase.TitleRow(right, 'Filament settings')
		configBase.SettingRow(right, 'filament_physical_density')
		configBase.SettingRow(right, 'filament_cost_kg')
		configBase.SettingRow(right, 'filament_cost_meter')

		configBase.TitleRow(right, 'Communication settings')
		configBase.SettingRow(right, 'serial_port', ['AUTO'] + machineCom.serialList())
		configBase.SettingRow(right, 'serial_baud', ['AUTO'] + map(str, machineCom.baudrateList()))

		configBase.TitleRow(right, 'Slicer settings')
		configBase.SettingRow(right, 'save_profile')

		configBase.TitleRow(right, 'SD Card settings')
		if len(profile.getSDcardDrives()) > 1:
			configBase.SettingRow(right, 'sdpath', profile.getSDcardDrives())
		else:
			configBase.SettingRow(right, 'sdpath')
		configBase.SettingRow(right, 'sdshortnames')

		configBase.TitleRow(right, 'Cura settings')
		configBase.SettingRow(right, 'check_for_updates')
		configBase.SettingRow(right, 'submit_slice_information')

		self.okButton = wx.Button(right, -1, 'Ok')
		right.GetSizer().Add(self.okButton, (right.GetSizer().GetRows(), 0), flag=wx.BOTTOM, border=5)
		self.okButton.Bind(wx.EVT_BUTTON, self.OnClose)
		
		self.MakeModal(True)
		main.Fit()
		self.Fit()

	def OnClose(self, e):
		if self.oldExtruderAmount != int(profile.getPreference('extruder_amount')):
			wx.MessageBox('After changing the amount of extruders you need to restart Cura for full effect.', 'Extruder amount warning.', wx.OK | wx.ICON_INFORMATION)
		self.MakeModal(False)
		self.parent.updateProfileToControls()
		self.Destroy()

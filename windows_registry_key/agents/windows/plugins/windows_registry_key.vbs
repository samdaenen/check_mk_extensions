' windows_registry_key - Windows Registry Key
'
' Copyright (C) 2020 Sam Daenen <sam.daenen@continu-it.be>
'
' This program is free software; you can redistribute it and/or
' modify it under the terms of the GNU General Public License
' as published by the Free Software Foundation; either version 2
' of the License, or (at your option) any later version.
'
' This program is distributed in the hope that it will be useful,
' but WITHOUT ANY WARRANTY; without even the implied warranty of
' MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
' GNU General Public License for more details.
'
' You should have received a copy of the GNU General Public License
' along with this program; if not, write to the Free Software
' Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
'
'
' Check, if we are executed with cscript.exe
If UCase(Right(Wscript.FullName, 11)) = "WSCRIPT.EXE" Then
    WScript.Echo "This script must be run under CScript."
    Wscript.Quit
End If

Dim regPaths
Dim windowsShell

' These two lines are set in the agent bakery
regPaths = Array("HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProductId","HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\WinStationsDisabled")

Set fso = CreateObject("Scripting.FileSystemObject")
Set objClass = GetObject("winmgmts:{impersonationLevel=impersonate}!\\.\root\cimv2")
Set wshShell = WScript.CreateObject( "WScript.Shell" )
remote_host = wshShell.ExpandEnvironmentStrings( "%REMOTE_HOST%" )
If remote_host = "%REMOTE_HOST%" Then
    remote_host = "local"
End If

' Handle error message ourselves so this script can also be run directly, for testing
On Error Resume Next

' Search Registry
If Not IsEmpty(regPaths) Then
	Wscript.Echo "<<<windows_registry_key>>>"
	For Each path in regPaths
	regValue = wshShell.RegRead(path)
    WScript.Echo path & "|" & regValue
Next
ElseIf IsEmpty(regPaths) Then
	Wscript.Echo "<<<windows_registry_key>>>"
	Wscript.Echo "No registry path found in parameters"
Else
	Wscript.Echo "<<<windows_registry_key>>>"
	Wscript.Echo "Unknown Error"
End If

WScript.Quit()

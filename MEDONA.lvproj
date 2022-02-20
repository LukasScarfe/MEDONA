<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="20008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="Full LabView Code.vi" Type="VI" URL="../Full LabView Code.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="LVPointTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVPointTypeDef.ctl"/>
				<Item Name="LVRectTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVRectTypeDef.ctl"/>
				<Item Name="VISA Configure Serial Port" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port"/>
				<Item Name="VISA Configure Serial Port (Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Instr).vi"/>
				<Item Name="VISA Configure Serial Port (Serial Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Serial Instr).vi"/>
			</Item>
			<Item Name="Current.vi" Type="VI" URL="../Current.vi"/>
			<Item Name="Droplet Size.vi" Type="VI" URL="../Droplet Size.vi"/>
			<Item Name="Evaporation Rate.vi" Type="VI" URL="../Evaporation Rate.vi"/>
			<Item Name="Height Suggestion.vi" Type="VI" URL="../Height Suggestion.vi"/>
			<Item Name="Initial Droplet Charge.vi" Type="VI" URL="../Initial Droplet Charge.vi"/>
			<Item Name="PythonVersionsEnum.ctl" Type="VI" URL="/C/Program Files (x86)/National Instruments/LabVIEW 2020/examples/Connectivity/Python/support/PythonVersionsEnum.ctl"/>
			<Item Name="Time For Evaporation.vi" Type="VI" URL="../Time For Evaporation.vi"/>
			<Item Name="ToPythonVersionString.vi" Type="VI" URL="/C/Program Files (x86)/National Instruments/LabVIEW 2020/examples/Connectivity/Python/support/ToPythonVersionString.vi"/>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="Medona Software" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{30CB147D-E4D0-413F-84A6-A72FDC5E185F}</Property>
				<Property Name="App_INI_GUID" Type="Str">{1F27AC3A-F5C9-4EA8-B3FF-AB489EA88906}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="App_serverType" Type="Int">0</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{0D2DBA9F-5AFB-4CD5-8743-2EEDFFF95EDD}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">Medona Software</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME/Medona Software</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{1BBA07D2-F3BA-45D3-A220-18718DB27391}</Property>
				<Property Name="Bld_version.build" Type="Int">7</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">Medona.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/Medona Software/Medona.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/Medona Software/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{DCBB8397-F8A8-400C-BDB4-AD66B8D663D1}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/Full LabView Code.vi</Property>
				<Property Name="Source[1].newName" Type="Str">Medona.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_fileDescription" Type="Str">Medona Software</Property>
				<Property Name="TgtF_internalName" Type="Str">Medona Software</Property>
				<Property Name="TgtF_productName" Type="Str">Medona Software</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{607EB914-27F2-4EA4-BA80-A7F60562F047}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">Medona.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
		</Item>
	</Item>
</Project>

# -*- coding: utf-8 -*-

line = 'NİLNİMNİŞNOMNOTNUHNUKNUNNURNUŞNÜHOBAODAOHAOHMOHŞOJEOKUOLEOMAONAONSONUORAORGOTOOVAOYAÖCÜÖDEÖGEÖĞEÖHÖÖKEÖLÇÖLÜÖMRÖRFÖRKÖRSÖRTÖRÜÖŞRÖTEÖZEÖZRPAÇPAKPALPANPASPATPAYPEÇPEDPEHPEKPERPESPEŞPETPEYPIRPITPİÇPİHPİKPİLPİMPİNPİRPİSPİŞPLİPOFPOGPOPPORPOSPOTPOYPOZPÖÇPÖFPÖHPUBPUÇPUDPUFPULPURPUSPUTPÜFPÜLPÜRRABRADRAFRAGRAHRAİRAMRANRAPRAYRAZREDREEREFREGREHREKREMRENRESRETREYREZRIHRİERİHRİKRİMRİŞRİVRODROKROLROMROPROTRUARUBRUDRUFRUHRUJRUMRUNRUSRUTRUYRUZRÜNSABSACSAÇSADSAFSAĞSAHSAİSAKSALSAMSANSAPSARSATSAVSAYSAZSEBSECSEÇSEGSEHSEKSELSEMSENSERSESSETSEVSEZSIĞSIKSIRSIZSİASİBSİFSİĞSİLSİMSİNSİRSİSSİTSİZSKİSOFSOKSOLSOMSONSOPSORSOSSOYSÖĞSÖKSÖNSÖRSÖVSÖZSPASUÇSUDSUFSUKSUNSUPSURSUSSUYSUZSÜBSÜMSÜNSÜRSÜSSÜTSÜZŞABŞADŞAHŞAKŞALŞAMŞANŞAPŞARŞAŞŞATŞAZŞEBŞEFŞEHŞEKŞEMŞENŞERŞEŞŞETŞEVŞEYŞIHŞIKŞIPŞIRŞİAŞİBŞİFŞİİŞİNŞİPŞİRŞİŞŞOKŞOLŞOMŞORŞOVŞUAŞUHŞUMŞURŞUTŞUYŞÜDŞÜŞTABTACTAÇTAİTAKTALTAMTANTAPTARTASTAŞTATTAVTAYTAZTEBTEFTEHTEKTELTEMTENTEPTERTEZTIĞTIKTINTIPTIRTISTİBTİCTİGTİĞTİHTİKTİMTİNTİPTİRTİZTOKTOLTONTOPTORTOSTOYTOZTÖRKÖSTÖZTRETUBTUFTUĞTUHTULTUMTUNTURTUŞTUTTUZTÜFTÜHTÜLTÜMTÜNTÜSTÜPTÜRTÜTTÜYUBUUCAUCBUDİUFOUHTUKMUKRULAULBULİULUUMKUNFUNKURAURFURSURYUSRUŞBUŞŞUTMUYUUZMUZOUZVÜHÜÜKLÜMMÜNSÜRDÜREÜRKÜRÜÜSRÜSSÜSTÜŞÜÜTÜÜYEÜZNVADVAHVAKVAMVANVARVATVAVVAYVAZVEAVEHVERVIKVINVIRVIZVİAVİPVURVÜSYADYAĞYAHYAKYALYANYAPYARYASYAŞYATYAVYAYYAZYEDYEGYEĞYEKYELYEMYENYERYESYETYEZYIĞYIKYILYIRYİNYİTYİVYİZYOĞYOKYOLYOMYORYOZYÖNYUFYUĞYUHYUMYUNYUTYUZYÜKYÜNYÜZZACZAÇZADZAGZAĞZALZAMZANZARZATZEDZELZEMZENZERZIHZILZIPZIRZITZİAZİBZİCZİHZİLZİNZOR'
n = 3
k=[line[i:i+n] for i in range(0, len(line), n)]
with open('klm3.txt', 'w') as f:
    for item in k:
        f.write("%s\n" % item)
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Python program to read
# json file

import pandas as pd
import json

IFCpath=r"/Users/vancekang/Library/CloudStorage/OneDrive-Personal/Work/SBCS/TS v1.3.3.json"
AnDpath2=r"/Users/vancekang/Library/CloudStorage/OneDrive-Personal/Work/SBCS/Project B V9_Modified TSD Model_95041.json"
# Opening JSON file
f = open(IFCpath)
f2 =open(AnDpath2)
# returns JSON object as
# a dictionary

data={
      "IFC": json.load(f),
      "AnD": json.load(f2)
      }

results_list=[]

#%%
# identifying data keys from AnD not in IFC
listA_D=[]
for i in data["AnD"].keys():
    if i not in list(data["IFC"].keys()):
        listA_D.append(i)

#%%
class StructuralModel:
    
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass
            
class StructuralMaterial:
    
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass

            
class StructuralCrossSection:
    
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass

class StructuralStorey:
    
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass
            
            
class StructuralPointConnection:
    
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass
    
class StructuralCurveMember:
    
    def __init__(self,data,ModelType):
        self.ModelType=ModelType

        pass

class StructuralSurfaceMember:
    
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass

class StructuralReinforcement:
    
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass

class StructuralUnit:
    
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass
    
class StructuralModelAnalysis:
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass
    
class StructuralModelDrift:
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass

class StructuralCode:
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass

class StructuralPointSupport:
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass

class StructuralLineSupport:
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass

class StructuralAreaSupport:
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass

class StructuralLoadGroup:
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass

class StructuralLoadCase:
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass

class StructuralLoadCombination:
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass

class StructuralCurveResult:
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass

class StructuralSurfaceResult:
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass
class StructuralPointReaction:
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass
    
class StructuralPointAction:
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass

class StructuralCurveAction:
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass

class StructuralSurfaceAction:
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass

class StructuralSteelDesign:
    def __init__(self,data,ModelType):
        self.ModelType=ModelType
        pass

#%%
    
# =============================================================================
# #%% IFC
# =============================================================================

# Entities with Name
IFC_Entities_with_Name=[]

for infodatatype in data["IFC"].keys():
    if data["IFC"][infodatatype] is None or len(data["IFC"][infodatatype])==0:
        pass
    elif "Name" in data["IFC"][infodatatype][0]:
        IFC_Entities_with_Name.append(infodatatype)
        
IFC_Entities_with_Name=set(IFC_Entities_with_Name)
            
# =============================================================================
# #%% AnD
# =============================================================================
# Entities with Name
AnD_Entities_with_Name=[]

for infodatatype in data["AnD"].keys():
    if data["AnD"][infodatatype] is None or len(data["AnD"][infodatatype])==0:
        pass
    
    elif "Name" in data["AnD"][infodatatype][0]:
        AnD_Entities_with_Name.append(infodatatype)

AnD_Entities_with_Name=set(AnD_Entities_with_Name)
    # if "Name" in AnD_data[infodatatype][0]:
    #     AnD_Entities_with_Name.append(infodatatype)
#%%

entity_mapping = {

    'StructuralModel':StructuralModel,
    'StructuralMaterial':StructuralMaterial,
    'StructuralCrossSection':StructuralCrossSection,
    'StructuralStorey':StructuralStorey,
    'StructuralPointConnection':StructuralPointConnection,
    'StructuralCurveMember':StructuralCurveMember,
    'StructuralSurfaceMember':StructuralSurfaceMember,
    'StructuralReinforcement':StructuralReinforcement,
    'StructuralUnit':StructuralUnit,
    'StructuralModelAnalysis':StructuralModelAnalysis,
    'StructuralModelDrift':StructuralModelDrift,
    'StructuralCode':StructuralCode,
    'StructuralPointSupport':StructuralPointSupport,
    'StructuralLineSupport':StructuralLineSupport,
    'StructuralAreaSupport':StructuralAreaSupport,
    'StructuralLoadGroup':StructuralLoadGroup,
    'StructuralLoadCase':StructuralLoadCase,
    'StructuralLoadCombination':StructuralLoadCombination,
    'StructuralCurveResult':StructuralCurveResult,
    'StructuralSurfaceResult':StructuralSurfaceResult,
    'StructuralPointReaction':StructuralPointReaction,
    'StructuralPointAction':StructuralPointAction,
    'StructuralCurveAction':StructuralCurveAction,
    'StructuralSurfaceAction':StructuralSurfaceAction,
    'StructuralSteelDesign':StructuralSteelDesign
        
}



#%%


def InstObject(data, ModelType,Entities_with_Name):
    
    for infodatatype in Entities_with_Name:
        ModelType=ModelType
        globals()[f"list_{infodatatype}"+"_"+ModelType]=[]
        list_of_entity_in_infodatatype=data[ModelType][infodatatype]
        # instantiating an object for each entity 
        for i in range(len(list_of_entity_in_infodatatype)):
            entity_item=list_of_entity_in_infodatatype[i]
            globals()[f"{entity_item['Name']}"+"_"+ModelType]=entity_mapping[infodatatype](data[ModelType],ModelType)
            globals()[f"{entity_item['Name']}"+"_"+ModelType].EntityType=f"{infodatatype}"
            #Dynamic attributes
            attributes_to_add = list(entity_item.keys())
            #Add these attributes dynamically and 
            for x in range(len(attributes_to_add)):
                setattr(globals()[f"{entity_item['Name']}"+"_"+ModelType], attributes_to_add[x], entity_item[attributes_to_add[x]])
            globals()[f"list_{infodatatype}"+"_"+ModelType].append(globals()[f"{entity_item['Name']}"+"_"+ModelType])
            
            
def InstObjectSubClass_IFC(data, ModelType,Entities_with_Name): 
    # assigning subclasses to objects
    for infodatatype in Entities_with_Name:
        list_of_entity_in_infodatatype=data[ModelType][infodatatype]
        # instantiating an object for each entity 
        for i in range(len(list_of_entity_in_infodatatype)):
            entity_item=list_of_entity_in_infodatatype[i]
            #Add these attributes dynamically and 
            if infodatatype=="StructuralCurveMember":
                globals()[f"{entity_item['Name']}"+"_"+ModelType].CrossSection=globals()[f"{entity_item['CrossSection']}"+"_"+ModelType]
                globals()[f"{entity_item['Name']}"+"_"+ModelType].Storey=globals()[f"{entity_item['Storey']}"+"_"+ModelType]
            if infodatatype=="StructuralCrossSection":
                globals()[f"{entity_item['Name']}"+"_"+ModelType].Material=globals()[f"{entity_item['Material']}"+"_"+ModelType]

    
#%%
# Creating IFC objects
InstObject(data=data, ModelType='IFC',Entities_with_Name=IFC_Entities_with_Name)
InstObjectSubClass_IFC(data=data, ModelType='IFC',Entities_with_Name=IFC_Entities_with_Name)
#%%
# Creating AnD objects
InstObject(data=data, ModelType='AnD',Entities_with_Name=AnD_Entities_with_Name)
# need to study the AnD data more 

# =============================================================================


#%%
class checks:
    def __init__(self):
        self.EntityType=""
        self.actualUnit=""
        self.actualValue=""
        self.elementId=""
        self.expectedValue=""
        self.expectedValueDataType=""
        self.fileID=""
        self.itemStatus=""


#%%

# define checks

#check16
def check16(IFCObj="",ADObj=""):
        if IFCObj.EndFixityEnd=="Free" or IFCObj.EndFixityStart=="Free":
            Checking=checks()
            Checking.EntityType=IFCObj.EntityType
            Checking.actualUnit="mm"
            Checking.actualValue=int(IFCObj.Length)
            Checking.elementId=IFCObj.Name
            Checking.expectedValue=8000
            Checking.expectedValueDataType=""
            Checking.fileID=""
            Checking.itemStatus=""
     
        # Checks for beam
            if Checking.actualValue>Checking.expectedValue:
                Checking.itemStatus="check16_warning"
            else:
                Checking.itemStatus="check16_pass"
                
            return Checking

#check17
def check17(IFCObj="",ADObj=""):
        if (IFCObj.EndFixityEnd in ['Pinned', 'Fixed']) and (IFCObj.EndFixityStart in ['Pinned', 'Fixed']):
            Checking=checks()
            Checking.EntityType=IFCObj.EntityType
            Checking.actualUnit="mm"
            Checking.actualValue=int(IFCObj.Length)
            Checking.elementId=IFCObj.Name
            Checking.expectedValue=20000
            Checking.expectedValueDataType=""
            Checking.fileID=""
            Checking.itemStatus=""
     
        # Checks for beam
            if Checking.actualValue>Checking.expectedValue:
                Checking.itemStatus="check17_warning"
            else:
                Checking.itemStatus="check17_pass"
                
            return Checking
#%%

for Obj in list_StructuralCurveMember_IFC:
    if Obj.Type=="Beam":
        # results_list.append(check1(IFCObj))
        # results_list.append(check2(IFCObj))
        # results_list.append(check3(IFCObj))
        # results_list.append(check4(IFCObj))
        # results_list.append(check5(IFCObj))
        # results_list.append(check6(IFCObj))
        # results_list.append(check7(IFCObj))
        # results_list.append(check8(IFCObj))
        results_list.append(check16(IFCObj=Obj))
        results_list.append(check17(IFCObj=Obj))

results_list = [item for item in results_list if item is not None]


#%%

print(list_StructuralCurveMember_IFC[0].CrossSection.Material.Name)



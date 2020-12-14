def equal_check(mol1,mol2): ##두개의 차를 확인. 입력은 mol
    dmol1=AllChem.DeleteSubstructs(mol1,mol2)
    dmol1=Chem.RemoveHs(dmol1)
    dmol2=AllChem.DeleteSubstructs(mol2,mol1)
    dmol2=Chem.RemoveHs(dmol2)
    d1_smart=Chem.MolToSmarts(dmol1)
    d2_smart=Chem.MolToSmarts(dmol2)
    if len(d1_smart)!=0:
        d1_smart_list=d1_smart.split('.')
        d1_smart_set=set(d1_smart_list)
        if d1_smart_set=={'[#1]'}:
            
            return 0
    else:        
        return 0
    if len(d2_smart)!=0:
        d2_smart_list=d2_smart.split('.')
        d2_smart_set=set(d2_smart_list)
        if d2_smart_set=={'[#1]'}:
            return 0
    else:        
        return 0
    return 1

##입력은 mol    
def equal_find(mol1,mol2): ##최대 공통부분을 찾은 뒤에, 각 분자구조와 최대 공통부분이 같은지를 확인하는 함수. 같으면 0, 다르면 1을 출력.
    listmol=[mol1,mol2]
    com_sub=rdFMCS.FindMCS(listmol)
    com_mol=Chem.MolFromSmarts(com_sub.smartsString)
    if (equal_check(mol1,com_mol)==0) or (equal_check(mol2,com_mol)==0):
        return 0
    else: return 1
print(equal_check(am,cm))

print(equal_find(am,cm))
print(equal_find(cm,am))

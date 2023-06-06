#Removes namespace other than the specified ones from the scene

for x in cmds.namespaceInfo(listOnlyNamespaces=True, recurse=True):
    #print(x)
    if x == 'test' or x =='example':
        print('no')
    else:
        print(x)
        cmds.namespace(removeNamespace=x, mergeNamespaceWithRoot=True)


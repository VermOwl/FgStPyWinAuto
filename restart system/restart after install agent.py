import os
import configparser

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

print (os.getcwd())
print (find('example.ini', os.getcwd()))
find_file = str(find('example.ini', os.getcwd()))

if (find_file == 'None'): #Если файла нету, мы его создаем
    print('Create ini files')
    config = configparser.ConfigParser()
    config['SYSTEM_IS_RESTART'] = {'system_hb_restarted' : 'False'}
    with open('example.ini', 'w') as configfile:
        config.write(configfile)
    system = config['SYSTEM_IS_RESTART']
    
    if system['system_hb_restarted'] == 'False': #проверяем если нада ли пререзагрузка, если да то меняем конфиг и перезагружаемся
        print ('System hasnt benn restarted')
        config['SYSTEM_IS_RESTART'] = {'system_hb_restarted' : 'True'}
        with open('example.ini', 'w') as configfile:
            config.write(configfile)
        os.system('shutdown -r -t 0')
    else:
        print ('System has been restarted')

else:
    config = configparser.ConfigParser()
    config.read('example.ini')

    print(config['SYSTEM_IS_RESTART']['system_hb_restarted'])

    if config['SYSTEM_IS_RESTART']['system_hb_restarted'] == 'False': #хз нахер я продублировал эту дичь, но вроде должно работать нормально
        print ('System hasnt benn restarted')
        config['SYSTEM_IS_RESTART'] = {'system_hb_restarted' : 'True'}
        with open('example.ini', 'w') as configfile:
            config.write(configfile)
        os.system('shutdown -r -t 0')
    else:
        print ('System has been restarted') # потом какое-то продолжение надо сделать

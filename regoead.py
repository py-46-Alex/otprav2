
import csv
import os
import re

codecs = ["cp1252", "cp437", "utf-16be", "utf-16", "utf-8"]

all_files = os.listdir()
to_delete = list(all_files)
# читаем адресную книгу в формате CSV в список contacts_list
if "phonebook.csv" in to_delete:
    os.remove("phonebook.csv")
    print('Начало работы... прошлый файл удален')

if "phonebooktested.csv" in to_delete:
    os.remove("phonebooktested.csv")


with open("phonebook_raw.csv", mode="r", encoding="utf-8") as filesok:
    rows = csv.reader(filesok, delimiter=",")
    contacts_list = list(rows)
    # print(contacts_list)

first_tro = contacts_list.pop(0)

for i in contacts_list:
    # print(i)
    la_list = []
    # print(i[1])
    # print(type(i[1]))
    # print(type(i[1]))
    koiu = i[1]
    # print(i[1])
    if koiu is None:
        deleted1 = i.pop(koiu)
    koiu2 = i[2]
    if koiu2 is None:
        deleted2 = i.pop(koiu2)
    # print(i)
    patrn1 = "\s"
    kop0 = re.sub(patrn1, ", ", i[0])  ## FAMIL
    # print(kop0)
    la_list.append(kop0)
    patrn2 = "\s"
    kop1 = re.sub(patrn2, ", ", i[1])  ##nM9l
    # # print(kop1)
    la_list.append(kop1)
    kop2 = i[2]                           ##  OT4ECTBO
    la_list.append(kop2)
    kop3 = i[3]                          ## oPpaHu3a
    la_list.append(kop3)
    kop4 = i[4]                           ## JOB
    la_list.append(kop4)
    patrn5 = r"(\+7|8)?\s*\((\d+)\)\s*(\d+)[\s-]*(\d+)[\s-]*(\d+)"
    chedngs = r"+7(\2)\3\4\5"
    kop5 = re.sub(patrn5, chedngs, i[5])
    # # print(kop5)
    var2 = kop5
    patrn51 = r"(\+7|8)?\s(\d+)[-](\d+)[-](\d+)"
    chngs51 = r"+7(\2)\3\4"
    kop51 = re.sub(patrn51, chngs51, var2)
    # # print(kop51)
    var3 = kop51
    patrn52 = r"(\+7)(\d)(\d)(\d)(\d+)"
    chngs52 = r"+7(\2\3\4)\5"
    kop52 = re.sub(patrn52, chngs52, var3)
    # # print(kop52)
    var4 = kop52
    patrn53 = r"(\+7)\s*[(](\d*)[)](\d*)\s*[(](\D)(\D)(\D)([.])\s*(\d*)[)]"
    chngs53 = r"+7\(\2)\3 \4\5\6.\8"
    kop53 = re.sub(patrn53, chngs53, var4)
    # # print(kop53)
    var5 = kop53
    patrn54 = r"(\+7)\s*[(](\d*)[)](\d*)\s*(\D)(\D)(\D)([.])(\s*)(\d*)"
    chngs54 = r"+7(\2)\3 \4\5\6.\9"
    kop54 = re.sub(patrn54, chngs54, var5)
    # print(kop54)
    var6 = kop54
    patrn55 = r"(\+7)\s*[\\][\\]*[(](\d*)[)](\d*)\s(\D)(\D)(\D)[.](\d*)"
    chns55 = r"+7(\2)\3 \4\5\6.\7"
    kop55 = re.sub(patrn55, chns55, var6)
    la_list.append(kop55)   ####TYT !!
    ### конец корректирови номера телефона
    kop6 = i[6]
    la_list.append(kop6)
    # print(la_list)
    # lopo = len(la_list)
    # print(lopo)
    with open("phonebooktested.csv", mode="a") as ffole:
        datawriter = csv.writer(ffole, delimiter=',', lineterminator="\r")
          # ##Вместо contacts_list подставьте свой список
        datawriter.writerow(la_list)
#


print("__________________________________________________________________________________________________")
name_list = []
with open("phonebooktested.csv", mode="r") as filesok2:
    rows = csv.reader(filesok2, delimiter=",")
    contacts_list2 = list(rows)

with open("phonebook.csv", mode="w") as ffole:
    datawriter = csv.writer(ffole, delimiter=',', lineterminator="\r")
    datawriter.writerow(first_tro)
###
with open("phonebooktested.csv", mode="w") as ffole:
    datawriter = csv.writer(ffole, delimiter=',', lineterminator="\r")
###


for rowes in contacts_list2:
    name_list = []
    # with open("phonebook.csv", mode="r") as filesok2:
    #     rows = csv.reader(filesok2, delimiter=",")
    #     contacts_list2 = list(rows)
    lastnamee = rowes[0]
    # print(zuba)
    pata = r'\s'
    prob = re.findall(pata, lastnamee)
    pro6eLL = (len(prob))
    if pro6eLL == 2:
        patrn0 = r"(['])?(\w*)?([,])?(\s)?(\w*)?([,])?(\s)?(\w*)?(['])?([,])?"
        chng0 = r'\2'
        lastname_change0 = re.sub(patrn0, chng0, lastnamee)
        # print(lastname_change0)
        name_list.append(lastname_change0)
        chng1 = r'\5'
        firs_name_normalized = re.sub(patrn0, chng1, lastnamee)
        # print(firs_name_normalized)
        name_list.append(firs_name_normalized)
        chng2 = r'\8'
        surname_norm = re.sub(patrn0, chng2, lastnamee)
        # print((surname_norm))
        name_list.append(surname_norm)
        # print(name_list)
    elif pro6eLL == 1:
        patrnlst = r"(['])?(\w*)?(['])?([, ])?(\s)?(['])?(\w*)?(['])?"
        chng2 = r'\2'
        surname_norm = re.sub(patrnlst, chng2, lastnamee)
        name_list.append(surname_norm)
        chng4 = r'\7'
        surname_norm4 = re.sub(patrnlst, chng4, lastnamee)
        name_list.append(surname_norm4)
        # print('ecTb 1 nPO6ELL')
    elif pro6eLL == 0:
        normal_name000 = str(lastnamee)
        name_list.append(normal_name000)  # нет пробелов добавлено 1 имя.

    not_normal_firstname = rowes[1]
    pata_not_normal_firstname = r'\s'
    pata_not_normal_prob = re.findall(pata_not_normal_firstname, not_normal_firstname)
    pata_not_normal_pro6eLL = (len(pata_not_normal_prob))
    # print(pata_not_normal_pro6eLL)
    this_is_normal_name = str(not_normal_firstname)
    if pata_not_normal_pro6eLL == 0:
        name_list.append(this_is_normal_name)
    elif pata_not_normal_pro6eLL == 1:
        patrn0 = r"(['])?(\w*)?([,])?(\s)?(\w*)?([,])?(\s)?(\w*)?(['])?([,])?"
        chng0 = r'\2'
        firstname_change0 = re.sub(patrn0, chng0, not_normal_firstname)
        name_list.append(firstname_change0)
        patternn01 = r"([,])?(\s)?(['])?(\w*)?([,])?(\s)?(\w*)?([,])?(\s)?(\w*)?(['])?([,])?(['])?"
        chng01 = r'\7'
        firstname_change1 = re.sub(patternn01, chng01, not_normal_firstname)
        name_list.append(firstname_change1)
    elif pata_not_normal_pro6eLL == 2:
        HET = None
        name_list.append(HET)

    not_normal_surname = rowes[2]
    pata_not_normal_surname = r'\s'
    pata_not_normal_surname_prob = re.findall(pata_not_normal_surname, not_normal_surname)
    surname_npo6eLL = len(pata_not_normal_surname_prob)
    if surname_npo6eLL == 0:
        DA = not_normal_surname
        name_list.append(DA)
    elif surname_npo6eLL == 1:
        xooo = None
        name_list.append(xooo)

    not_normal_organization = rowes[3]
    # print(not_normal_organization)
    org_len = len(not_normal_organization)
    if org_len >= 1:
        name_list.append(not_normal_organization)
    else:
        HET = None
        name_list.append(HET)

    not_normal_pozition = rowes[4]
    pozit_len = len(not_normal_pozition)
    if pozit_len >= 2:
        name_list.append(not_normal_pozition)
    else:
        HET = None
        name_list.append(HET)  # нет должноти

    already_normal_phone = rowes[5]
    # print(already_normal_phone)
    phone = str(already_normal_phone)
    check_phone = len(phone)
    if check_phone >= 1:
        name_list.append(phone)
    else:
        HET = None
        name_list.append(HET)  # нет телефона

    email = rowes[6]
    norm_mail = str(email)
    check_mail = len(norm_mail)
    # print(check_mail)
    if check_mail >= 2:
        name_list.append(norm_mail)
    else:
        HET = None
        name_list.append(HET)  # нет емейла
    list_half_ready = list(name_list)
    for item in list_half_ready:
        quest_org = list_half_ready[3]
        if len(list_half_ready) > 7:
            list_half_ready.remove(quest_org)
    with open("phonebook.csv", mode="a") as ffole:
        datawriter = csv.writer(ffole, delimiter=',', lineterminator="\r")
          # ##Вместо contacts_list подставьте свой список
        datawriter.writerow(list_half_ready)
    with open("phonebooktested.csv", mode="a") as ffole:
        datawriter = csv.writer(ffole, delimiter=',', lineterminator="\r")
          # ##Вместо contacts_list подставьте свой список
        datawriter.writerow(list_half_ready)

# print('B OPurUHAJlE')
# for nu in contacts_list2:
#     print(nu)

# print('B roBHE')
with open("phonebooktested.csv", mode="r") as filesok22:
    rows = csv.reader(filesok22, delimiter=",")
    contactss = list(rows)

new_contacts_list = list(contactss)
# connta = set()
# for i in new_contacts_list:
#     print(i)
#     lasnam = i[0]
#     uM9i = i[1]
#     surname = i[2]
#     org = i[3]
#     dolgn = i[4]
#     telefon = i[5]
#     emeil = i[6]
#     for t2 in new_contacts_list:
#         if lasnam == t2[0] and uM9i == t2[1] and surname == t2[2]:
#             lastnam = t2[0]
#             connta.append(lastnam)
#             fisna = t2[1]
#             connta.append(fisna)
#             surename = t2[2]
#         else:
# И ВОТ НА ЭТОМ ЭТАПЕ
#я  не понимаю как мне удалить итоговые дублиаты. файл в нужном виде я получил. дубликаты удалить немогу. пробывал удалиить через сет. 
# но сет не работает со списками. 
if "phonebooktested.csv" in to_delete:
    os.remove("phonebooktested.csv")



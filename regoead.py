import csv
import os
import re
from collections import Counter

codecs = ["cp1252", "cp437", "utf-16be", "utf-16", "utf-8"]
#
def normilized_file_writer(normilazed_contact_list):
    with open("phonebook.csv", mode="w") as file:
        datawriter_of_file = csv.writer(file, delimiter=',', lineterminator="\r")
        datawriter_of_file.writerows(normilazed_contact_list)
#
def normalaizer():
    with open("phonebook_raw.csv", mode="r") as filesok:
        rows = csv.reader(filesok, delimiter=",")
        contacts_list = list(rows)
    for i in contacts_list:
        la_list = []
        patrn1 = "\s"
        kop0 = re.sub(patrn1, ", ", i[0])
        la_list.append(kop0)
        patrn2 = "\s"
        kop1 = re.sub(patrn2, ", ", i[1])
        la_list.append(kop1)
        kop2 = i[2]
        la_list.append(kop2)
        kop3 = i[3]
        la_list.append(kop3)
        kop4 = i[4]
        la_list.append(kop4)
        patrn5 = r"(\+7|8)?\s*\((\d+)\)\s*(\d+)[\s-]*(\d+)[\s-]*(\d+)"
        chedngs = r"+7(\2)\3\4\5"
        kop5 = re.sub(patrn5, chedngs, i[5])
        var2 = kop5
        patrn51 = r"(\+7|8)?\s(\d+)[-](\d+)[-](\d+)"
        chngs51 = r"+7(\2)\3\4"
        kop51 = re.sub(patrn51, chngs51, var2)
        var3 = kop51
        patrn52 = r"(\+7)(\d)(\d)(\d)(\d+)"
        chngs52 = r"+7(\2\3\4)\5"
        kop52 = re.sub(patrn52, chngs52, var3)
        var4 = kop52
        patrn53 = r"(\+7)\s*[(](\d*)[)](\d*)\s*[(](\D)(\D)(\D)([.])\s*(\d*)[)]"
        chngs53 = r"+7\(\2)\3 \4\5\6.\8"
        kop53 = re.sub(patrn53, chngs53, var4)
        var5 = kop53
        patrn54 = r"(\+7)\s*[(](\d*)[)](\d*)\s*(\D)(\D)(\D)([.])(\s*)(\d*)"
        chngs54 = r"+7(\2)\3 \4\5\6.\9"
        kop54 = re.sub(patrn54, chngs54, var5)
        var6 = kop54
        patrn55 = r"(\+7)\s*[\\][\\]*[(](\d*)[)](\d*)\s(\D)(\D)(\D)[.](\d*)"
        chns55 = r"+7(\2)\3 \4\5\6.\7"
        kop55 = re.sub(patrn55, chns55, var6)
        la_list.append(kop55)
        kop6 = i[6]
        la_list.append(kop6)
        with open("phonebooktested.csv", mode="a") as ffole:
            datawriter = csv.writer(ffole, delimiter=',', lineterminator="\r")
            datawriter.writerow(la_list)

def datawriter():
    HET = None
    with open("phonebooktested.csv", mode="r") as filesok2:
        rows = csv.reader(filesok2, delimiter=",")
        contacts_list2 = list(rows)
    for rowes in contacts_list2:
        name_list = []
        lastnamee = rowes[0]
        pata = r'\s'
        prob = re.findall(pata, lastnamee)
        pro6eLL = (len(prob))
        if pro6eLL == 2:
            patrn0 = r"(['])?(\w*)?([,])?(\s)?(\w*)?([,])?(\s)?(\w*)?(['])?([,])?"
            chng0 = r'\2'
            lastname_change0 = re.sub(patrn0, chng0, lastnamee)
            name_list.append(lastname_change0)
            chng1 = r'\5'
            firs_name_normalized = re.sub(patrn0, chng1, lastnamee)
            name_list.append(firs_name_normalized)
            chng2 = r'\8'
            surname_norm = re.sub(patrn0, chng2, lastnamee)
            name_list.append(surname_norm)
        elif pro6eLL == 1:
            patrnlst = r"(['])?(\w*)?(['])?([, ])?(\s)?(['])?(\w*)?(['])?"
            chng2 = r'\2'
            surname_norm = re.sub(patrnlst, chng2, lastnamee)
            name_list.append(surname_norm)
            chng4 = r'\7'
            surname_norm4 = re.sub(patrnlst, chng4, lastnamee)
            name_list.append(surname_norm4)
            name_list.append(HET)
        elif pro6eLL == 0:
            normal_name000 = str(lastnamee)
            name_list.append(normal_name000)
        not_normal_firstname = rowes[1]
        pata_not_normal_firstname = r'\s'
        pata_not_normal_prob = re.findall(pata_not_normal_firstname, not_normal_firstname)
        pata_not_normal_pro6eLL = (len(pata_not_normal_prob))
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
            name_list.append(HET)
        name_list.append(HET)
        not_normal_organization = rowes[3]
        org_len = len(not_normal_organization)
        if org_len >= 1:
            name_list.append(not_normal_organization)
        else:
            name_list.append(HET)
        not_normal_pozition = rowes[4]
        pozit_len = len(not_normal_pozition)
        if pozit_len >= 2:
            name_list.append(not_normal_pozition)
        else:
            name_list.append(HET)
        already_normal_phone = rowes[5]
        phone = str(already_normal_phone)
        check_phone = len(phone)
        if check_phone >= 1:
            name_list.append(phone)
        else:
            name_list.append(HET)  # нет телефона
        email = rowes[6]
        norm_mail = str(email)
        check_mail = len(norm_mail)
        if check_mail >= 2:
            name_list.append(norm_mail)
        else:
            name_list.append(HET)
        list_half_ready = list(name_list)
        listi_to_write = []
        for item in list_half_ready:
            quest_org = list_half_ready[3]
            if len(list_half_ready) > 7:
                list_half_ready.remove(quest_org)
            listi_to_write.append(item)
        with open("phonebooktemp.csv", mode="a") as ffole:
            datawriter = csv.writer(ffole, delimiter=',', lineterminator="\r")
            datawriter.writerow(listi_to_write)
#
def new_temp_row():
    with open("phonebooktemp.csv", mode="r") as f:
        rows = csv.reader(f, delimiter=",")
        contactss = list(rows)
    new_temp = list(contactss)
    return new_temp
#
def delete_duplicates_contact(list1):
    phone_book = dict()
    for contact in list1:
        if contact[0] in phone_book:
            # print(contact[0])
            contact_value = phone_book[contact[0]]
            # print(contact_value)
            for i in range(len(contact_value)):
                if contact[i]:
                    # print(contact_value[i])
                    # print(contact[i])
                    contact_value[i] = contact[i]
        else:
            phone_book[contact[0]] = contact
        # print(phone_book)
    phones_all = list(phone_book.values())
    return phones_all
#
def delete_temp_files():
    all_files = os.listdir()
    to_delete = list(all_files)
    if "phonebooktested.csv" in to_delete:
        os.remove("phonebooktested.csv")
    if "phonebooktemp.csv" in to_delete:
        os.remove("phonebooktemp.csv")


def activate_normalize():
    """" Основная логика """
    normalaizer()
    datawriter()
    new_temp = new_temp_row()
    phons_all = delete_duplicates_contact(new_temp)
    normilized_file_writer(phons_all)
    delete_temp_files()
#
if __name__ == '__main__':
    activate_normalize()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    
    f_sql, f_txt = open('user_data_only.sql','r'), open('mail_list.txt','w')
    
    t, n = '\t', '\n'
    
    f_txt.write('Nombre' + t + 'Email' + t + 'Usuario' + n)
    
    mail_list_a, mail_list_b = '', ''
    
    for line in f_sql:
        
        if t in line:
            
            data = line.split(t)
            
            f_txt.write(data[4].strip() + t + data[2].strip() + t + data[3].strip() + n)
            
            mail_list_a += data[4].strip() + '<' + data[2].strip() + '>;'
            mail_list_b += data[2].strip() + ';'
        
    f_txt.write(n)
    f_txt.write(mail_list_a)
    f_txt.write(n * 2)
    f_txt.write(mail_list_b)
    
    f_txt.close()
    f_sql.close()

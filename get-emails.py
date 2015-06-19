#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3 as published by
the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/gpl-3.0.txt>.
'''

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

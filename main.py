import datetime
# from file_recovery import read_recovery_file, write_recovery_file
from download import downloads
from file_recovery import write_recovery_file, read_recovery_file
import argparse

def get_today_files(file_id):
    return [
        f'https://links.sgx.com/1.0.0/derivatives-historical/{file_id}/WEBPXTICK_DT.zip',
        f'https://links.sgx.com/1.0.0/derivatives-historical/{file_id}/TickData_structure.dat',
        f'https://links.sgx.com/1.0.0/derivatives-historical/{file_id}/TC_.txt',
        f'https://links.sgx.com/1.0.0/derivatives-historical/{file_id}/TC_structure.dat'
    ]

def define_url(custome=None):
    base_id = 5531
    base_day = 2
    base_week = 42
    if custome:
        today = datetime.date.today()
    else:
        print('Nhap nam, thang, ngay: ')
        year = int(input())
        month = int(input())
        day = int(input())
        today = datetime.date(year, month, day)

    week_number = today.isocalendar().week
    weekday = today.weekday()
    file_time = str(today)

    if weekday < 5:
        if week_number == 42:
            if weekday == 2:
                file_id = 5531
            else:
                file_id = base_id + weekday - 2
        if week_number > 42:
            file_id = base_id + 5*(week_number-base_week-1) + base_day + weekday + 1
        if week_number < 42:
            file_id = base_id - 5*(base_week-week_number-1) - base_day - 5 + weekday
    return file_id,file_time

def main():
    recovery_url = read_recovery_file('recovery.txt')
    print(recovery_url)
    if recovery_url:
        for string in recovery_url:
            index = string.rfind("/")
            url = string[:index]
            date_file = string[index+1:]
            failed_urls = downloads(url, date_file)
            write_recovery_file('recover.txt', failed_urls)
            print("co vao day khog")

    define = define_url(1)
    url_list = get_today_files(define[0])
    url_failed = downloads(url_list, define[1]) # download file today
    write_recovery_file('recovery.txt', url_failed)




    # write_recovery_file = ('/Users/thieuquangbach/Desktop/data_sgx/recover.txt', failed_url)

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download files from the specified website.')
    parser.add_argument('--id', help='File ID corresponding to the date', required=False, type=str)
    args = parser.parse_args()
    
    main()
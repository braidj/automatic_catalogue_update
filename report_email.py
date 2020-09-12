#!/usr/bin/env python3
import reports
import emails
import os
from datetime import date

def generate_report_detail():

    DESC_DIR = '/home/braid/development/automatic_catalogue_update/supplier-data/descriptions'
    desc_files = [x for x in os.listdir(DESC_DIR) if 'txt' in x] # only want .txt
    nl = "<br/>"

    results={}
    formatted=[]

    for f in desc_files:
        current_file=f"{DESC_DIR}/{f}"
        with open(current_file,'r') as desc_details:

            raw_lines = desc_details.readlines()
            clean_lines = [x.strip() for x in raw_lines]

            fruit = clean_lines[0]
            weight = clean_lines[1]

        results[fruit]=weight

    #print(results)
    for key in sorted(results.keys()) :# sort the dictionary on key
        #print(f"name:{key}{nl}weight:{results[key]}{nl}")
        formatted.append(f"name: {key}{nl}weight: {results[key]}{nl}")

    #print(formatted)
    return nl.join(formatted)

if __name__ == "__main__":

    detail = generate_report_detail()
    today = date.today()
    format_today = today.strftime("%B %d, %Y")
    title = f"Processed update on {format_today}"

    reports.generate_report("/tmp/processed.pdf",title,detail)

    from_user="automation@example.com"
    username="!!TBC!!@example.com"
    subject="Upload Completed - Online Fruit Store"
    body="All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    msg = emails.generate(from_user,username,subject,body,"/tmp/processed.pdf")
    emails.send(msg)

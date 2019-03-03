import os
import csv


TotalVotes = 0
VoteDetails = {}
nameexists = False
winner =0
winnername=""


csvpath = os.path.join("resources","election_data.csv")

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
   
    for row in csvreader:
        TotalVotes +=1
        CandidateName = row[2]
        if CandidateName not in VoteDetails:
            VoteDetails[row[2]] = 1  #'Inserting the candidate to the dictionary'
        else:
            VoteDetails[CandidateName] += 1     #'Updating the candidate vote in the dictionary'

    print("Election Results")
    print("-----------------")
    print(f"Total Votes: {TotalVotes}")
    print("-----------------")
    for k, v in VoteDetails.items():
        VotePercent = round((v/TotalVotes)*100,3)
        if v > winner:
            winner = v
            winnername =k
        print(f"{k} : {VotePercent}% ({v})")

    print("-----------------")
    print(f"Winner : {winnername}")
    print("-----------------")

output_path = os.path.join("output", "Election Results.txt")

with open(output_path, 'w', newline="\n") as txtFile:

      print("Election Results" , end ='\n', file = txtFile)
      print("----------------" ,end ='\n', file = txtFile)
      print(f"Total Votes: {TotalVotes}", file = txtFile)
      print("-----------------" , file = txtFile)
      for k, v in VoteDetails.items():
        VotePercent = round((v/TotalVotes)*100,3)
        print(f"{k} : {VotePercent}% ({v})" , end ='\n', file = txtFile)
      print("------------------" ,end ='\n', file = txtFile)
      print(f"Winner : {winnername}", file=txtFile)
      print("------------------" ,end ='\n', file = txtFile)

    
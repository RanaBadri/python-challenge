import csv



filename = "election_data.py"
with open("election_data.csv",'r') as election_results:
  election_results = csv.reader(election_results,delimiter=",")

  
  total_votes = 0 
  candidates_stats = 0
  candidates = {}
  count = 0 
  header = next(election_results)
  
  for row in election_results:
    #find and print the total votes
    #retreive total only?
    total_votes = total_votes + 1
      
    if row[2] not in candidates:
      candidates [row[2]] = 1
    candidates [row[2]] += 1
   
  winningVote = 0
  winner = ""

  for Candidate, vote in candidates.items ():
    if vote > winningVote:
      winner = Candidate
      winningVote =vote
   
  Candidates = "" 
         
  def print_percentages(candidates_results):

  # Find the total number of matches wrestled
    Candidates_Votes = int(candidates_results[1])
  

# Find the percentage of matches won
percente_votes = Candidates / total_votes *100



# Print out the wrestler's name and their percentage stats



    
print(total_votes)
print(candidates)
print ('Candidates: ' + candidates_stats[0])
print('Candidates_Votes: {round(percent_votes,1)}%')
print(winner)
   
with open("output.txt", "w") as text_file:
    text_file.write(f"Total Votes are:{total_votes} \n Candidates summary: {candidates}")
    text_file.write(f" \n Percentage of votes per candidate is: {round(percent_votes,1)}%")   
    text_file.write(" \n winner is: {winner}")
    
teilnehmer = (
    'Eva',
    'Sascha',
    'Philip',
    'Reinhard',
    'Marcus',
    'Peter',
    'Leo',
)

participants = list(teilnehmer)
participants.append('Mark')
print(participants)

participants_original = list(participants)
## print(participants.sort()) - retourniert None

participants.sort()
print(participants)
print(participants_original)

print(participants[1:4])

del(participants[3])


participants.remove('Leo')
print(participants)
print(participants.count('Leo'))
print(participants.index('Peter'))

print(participants[len(participants)-1])

for participant in participants:
    print(participant)

print(participants.pop(0))
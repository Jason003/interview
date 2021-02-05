import collections
def invalidBadgeRecords(records):
    entered = set()
    enterWithoutBadge = set()
    exitWithoutBadge = set()
    for name, flag in records:
        if flag == 'enter':
            if name in entered:
                enterWithoutBadge.add(name)
            else:
                entered.add(name)
        else:
            if name not in entered:
                exitWithoutBadge.add(name)
            else:
                entered.remove(name)
    return list(enterWithoutBadge | entered), list(exitWithoutBadge)

badge_records = [
   ["Martha",   "exit"],
   ["Paul",     "enter"],
   ["Martha",   "enter"],
   ["Martha",   "exit"],
   ["Jennifer", "enter"],
   ["Paul",     "enter"],
   ["Curtis",   "enter"],
   ["Paul",     "exit"],
   ["Martha",   "enter"],
   ["Martha",   "exit"],
   ["Jennifer", "exit"],
 ]
print(invalidBadgeRecords(badge_records))


def frequentAccess(records):
    if not records:
        return []
    result = []
    times = collections.defaultdict(list)
    for name, timestamp in records:
      times[name].append(timestamp)
    def timeDifference(a, b):
      a, b = int(a), int(b)
      aHour = a//100
      bHour = b//100
      aMinute = a % 100
      bMinute = b % 100
      return  (bHour * 60 + bMinute) - (aHour * 60 + aMinute)

    for name, timestamps in times.items():
        timestamps.sort()
        i = 0
        timewindow = [timestamps[i]]
        for j in range(1, len(timestamps)):
          if (timeDifference(timestamps[i], timestamps[j]) <= 60):
            timewindow.append(timestamps[j])
          else:
            timewindow = [timestamps[j]]
            i = j
        if len(timewindow) >= 3:
          result.append([name, timewindow])
    return result


print(frequentAccess([['James', '1259'], ['James', '1200'], ['James', '1220'], ['Martha', '1600'], ['Martha', '1620'], ['Martha', '1530']]))

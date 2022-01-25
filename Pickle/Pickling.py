import pickle

# imelda = ('More Mayhem',
#           'IMelda May',
#           '2011',
#           ((1, 'Pulling the Rug'),
#            (2, 'Psycho'),
#            (3, 'Mayhem'),
#            (4, 'Kentish Town Waltz')))
#
# with open("imelda.pickle", 'bw') as pickle_file:
#     pickle.dump(imelda, pickle_file)
#
# with open("imelda.pickle", 'br') as imelda_pickled:
#    imelda2 = pickle.load(imelda_pickled)
#
# print(imelda2)
#
# album, artist, year, tracks = imelda2
# print(album)
# print(artist)
# print(year)
# for track in tracks:
#     track_number, track_title = track
#     print(track_number, track_title)


imelda = ('More Mayhem',
          'IMelda May',
          '2011',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')))
even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open("imelda.pickle", 'bw') as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)        # Protocol used to encrypt in binary file, no need to give
    pickle.dump(even, pickle_file, protocol=2)          # protocol while loading python automatically  detects protocol
    pickle.dump(odd, pickle_file, protocol=1)           # we can use more than one protocol
    pickle.dump(1816510088, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump("NAQEEB '.' ", pickle_file,protocol=0)

with open("imelda.pickle", 'br') as imelda_pickled:
   imelda2 = pickle.load(imelda_pickled)                # load pickle in same order as they are dumped
   even = pickle.load(imelda_pickled)
   odd = pickle.load(imelda_pickled)
   r = pickle.load(imelda_pickled)
   na = pickle.load(imelda_pickled)

print(imelda2)

album, artist, year, tracks = imelda2
print(album)
print(artist)
print(year)
for track in tracks:
    track_number, track_title = track
    print(track_number, track_title)

print("="*20)

for i in even:
    print(i)

print("="*20)

for i in odd:
    print(i)

print("="*20)
print(r)
print(na)

## deletes pickle file
# pickle.loads(b"cos\nsystem\n(S'rm imelda.pickle'\ntR.")  # linux or mac
# pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR.")  # windows
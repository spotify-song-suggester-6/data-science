
"""
EXAMPLE FILE

how to implement knn-based suggestion engine, v.1


### NOTE: ###

model seems to ONLY accept DF-style 2D arrays as input,
input needs to have shape of (1, 13), and
input needs to NOT have columns: "track_id",
								 "artist_name",
								 "track_name",
								 "duration_ms"

"""


import joblib

FILENAME = 'model-v1.sav'


def kayDeeSuggestsThis(FILENAME, songInputVarGoesHere, df):

	# load model from saved serialized file
	kayDeeTree = joblib.load( FILENAME)

	# query model with input song's features,
	# outputting 11 songs' indices and their distances from original input
	dist, ind = kayDeeTree.query(songInputVarGoesHere, k= 11)

	# display suggested songs' index values, distances from original input
	# in array form
	print(ind)
	print(dist)

	# return main dataframe, masked by returned indices
	# sliced 1:11 as the input song is returned in the list at location 0, but
	# we still want 10 songs
	return df.iloc[ind[0][1:11]]

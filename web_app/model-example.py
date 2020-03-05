
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


def kayDeeSuggestsThis(FILENAME, songInputVars, df):
	"""Loads model from saved file and uses it to generate 10 similar songs.

		This function loads a saved external pickled K-nearest-neighbors model
	with joblib. It then uses that model to take in specified song features
	and return a data frame containing the 10 most similar songs.

	Arguments:
		FILENAME {string} - the path to the pickled model.
		songInputVars {data frame} - (1, 13)-shaped data frame of features.
		df {data frame} -- The data frame with the song data to be modeled.

	Returns:
		{data frame} -- A (10, 18)-shape data frame containing acoustic and
		identifying data for the 10 most similar songs.
	"""
	kayDeeTree = joblib.load(FILENAME)

	# query model with input song's features,
	# outputting 11 songs' indices and their distances from original input
	dist, ind = kayDeeTree.query(songInputVars, k=11)

	# display suggested songs' index values, distances from original input
	# in array form
	print(ind)
	print(dist)

	# return main dataframe, masked by returned indices
	# sliced 1:11 as the input song is returned in the list at location 0, but
	# we still want 10 songs
	return df.iloc[ind[0][1:11]]

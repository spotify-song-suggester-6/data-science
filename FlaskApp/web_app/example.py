""" 
EXAMPLE FILE 

how to implement suggestion engine 

(potentially -- this doesn't feel complete to me)

"""




"""

import joblib


def suggestSong( inputList):

	'''
 		Instantiate list of track_ids to be returned with whatDoesThisDo

		Then open serialized ML weights file (core of suggestion engine)
			and instantiate as model
	'''

	whatDoesThisDo = []
	with open( 'model(v0).sav') as pred:
		model = joblib.load( pred)


	for track in inputList:
		'''
			For each track_id passed to us, reference that against db to retreive
				rest of song feature data
			Then run that array through suggestion engine and return list of
				suggested results
		'''

		t = text( "SELECT * FROM Song WHERE track_id IN (:trackID);")

#			curse = db cursor (create_engine().connect())
		songInput = curse.execute( t, trackID= track)
		referenceData = songInput.fetchall()
		referenceData = list( referenceData[0])

		songData = referenceData

		whatDoesThisDo = model.predict( [[songData]])

		return whatDoesThisDo
		
"""
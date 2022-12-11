import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")


Datafile_path = "/config/workspace/aps_failure_training_set1.csv"
Database_name = "Aps"
Collection_name = "Sensor"

if __name__=="__main__":
    df = pd.read_csv(Datafile_path)
    print(f"Rows and columns: {df.shape}")

    # convert data frame to jason format for dumping 
    df.reset_index(drop = True, inplace = True)

    json_record = list(json.loads(df.T.to_json()).values())
    #print(json_record[0])

    # insert converted json record to mongodb
    client[Database_name][Collection_name].insert_many(json_record)

    

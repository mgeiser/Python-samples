
import json

test_dictionary = {'family_id':"family_id",
'individual_id':"Mgeiser",
'sex':"M",
'age':51,
'pcp':"3456",
'spec':3453,
'inpatient':2,
'pregnant':1,
'raw_costs':"34.25",
'raw_utilization':"25.25",
'drugs':"none",
'diagnoses':"none",}




def format_features(d):
    # convert values to proper types
    r = {}
    for k, v in d.items():
        if v == 'False':
            v = False
        if v == 'True':
            v = True

        # leave them as strings
        if k in ('family_id', 'individual_id', 'sex'):
            r[k] = str(v)
        # convert to ints
        elif k in {'age', 'pcp', 'spec', 'inpatient'}:
            r[k] = int(float(v))
        # convert to booleans
        elif k == 'pregnant':
            # value comes in as 1 or 0; 1 = True, 0 = False
            r[k] = bool(float(v))
        # keep floats
        elif k == 'raw_costs':
            r[k] = float(v)
        elif k == 'raw_utilization':
            r['raw_costs'] = float(v)
        elif k in ('log_raw_costs', 'no_drugs'):
            # ignore columns that could be created by transforms
            pass
        # only include drugs if they are 1 (sparsification)
        elif k in {'drugs', 'diagnoses'}:
            if v in("none","None", ""):
                r[k] = None
            else:
                r[k] = set(v)
        elif k == 'detailed_costs':
            r[k] = list(v)
        elif k in ['medical_allowed', 'drug_allowed']:
            pass
        else:
            raise NotImplementedError('Unknown key {}'.format(k))

    return r



print("\n\n")
print(json.dumps(test_dictionary, indent=4, sort_keys=True))
print("\n\n")
test = format_features(test_dictionary)
try:
    print(json.dumps(test, indent=4, sort_keys=True))
    # print(test)
except Exception as e:
    print(e)


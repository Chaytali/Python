def fromkeys(input_dict,output_dict_values):
    result_dict={}
    if type(output_dict_values)==list or type(output_dict_values)==tuple:
        keys_list=input_dict.keys()
        values_length=len(output_dict_values)
        for i in range(len(keys_list)):
            if i < values_length:
                result_dict[keys_list[i]]=output_dict_values[i]
                
            else:
                result_dict[keys_list[i]]=none
        print result_dict       


if(__name__=="__main__"):
    fromkeys({1:1,2:2,3:3},[100,200,300])
                

DIM_IVR_Rules = {'columns':['IVR_Rule_ID','IVR_Rule_Description','RI_Ind'],
                'dataset':'DW_Operations',
                'source_tb':'DIM_IVR_Rules',
                'target_tb':'DIM_IVR_Rules_GCP',
                'pk_list':['IVR_Rule_ID']}
DIM_Emails =  {'columns':['Email_ID','Email_Name','RI_Ind'],
                'dataset':'DW_Others',
                'source_tb':'DIM_Emails',
                'target_tb':'DIM_Emails_GCP',
                'pk_list':['Email_ID']}
DIM_Account_Types = {'columns':['Account_Type_ID','Account_Type_Desc','RI_Ind'],
                'dataset':'DW_Others',
                'source_tb':'DIM_Account_Types',
                'target_tb':'DIM_Account_Types_GCP',
                'pk_list':['Account_Type_ID']}
DIM_Affiliate_Offers = {'columns':['Offer_ID','Offer_Desc','RI_Ind'],
                'dataset':'DW_Others',
                'source_tb':'DIM_Affiliate_Offers',
                'target_tb':'DIM_Affiliate_Offers_GCP',
                'pk_list':['Offer_ID']}
DIM_Affiliate_Statuses = {'columns':['Status_ID','Status_Description'],
                'dataset':'DW_Others',
                'source_tb':'DIM_Affiliate_Statuses',
                'target_tb':'DIM_Affiliate_Statuses_GCP',
                'pk_list':['Status_ID']}
DIM_Affiliates = {'columns':['Affiliate_ID','Name','Address1','Address2','City','Zipcode','Country_ID','Phone'],
                'dataset':'DW_Others',
                'source_tb':'DIM_Affiliates',
                'target_tb':'DIM_Affiliates_GCP',
                'pk_list':['Affiliate_ID']}
                     
                      
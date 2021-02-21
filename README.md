 S3 Monitor
--------------------------

Project created for the Coveo DevOps Challenge

 Usage
---------------------
Recommendation:  
 Although the idea of running all the buckets in the account at the same time is great, I believe the execution of this script should be associated to an orchestrator, such as Jenkins.  
 You can then break the execution by a region or storage type. They can run in parallel and using different AWS API sessions. Once all of them return, we can just aggregate the responses.     


Prerequisites:
- Python  
    - https://www.python.org/downloads/
    - Version 3.9
- Boto3
    - https://pypi.org/project/boto3/
    - Version 1.16.19
    
Help:  
- ```python3 s3_monitor.py -h```  

Examples:  
- ```python3 s3_monitor.py -p user1-dev```
- ```python3 s3_monitor.py -p user1-dev -r us-east-2```
- ```python3 s3_monitor.py -p user1-dev -b my-bucket```
- ```python3 s3_monitor.py -p user1-dev -r us-west-1 -s StandardStorage```
- ```python3 s3_monitor.py -p user1-dev -s GlacierStorage```

Options:

| Options | Value | Mandatory |
| ------- | ----- | --------- |
| -h  | Displays help message.<br>When used it will disregard the other options | no |
| -p  | AWS Profile to process the routine - e.g. user1-dev  | **YES** |
| -r  | Specific region to run the tool                      | no |
| -b  | Specific bucket to run the tool                      | no |
| -s  | Specific storage type to get information from        | no |


**INFO**  
How to set up your AWS profile? [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html)
------------------------------------------------------------------------------------
Outputs
---------------------
JSON Object with a list of buckets and their information
```JSON
[
  {
    "name": "my-bucket",
    "creation_date": "2020-05-04 15:13:08+00:00",
    "region": "us-east-1",
    "storage": {
      "StandardStorage": {
        "size": 440440195.0,
        "cost": 0.01
      }
    },
    "total_size": 440440195.0,
    "total_cost": 0.01,
    "num_objects": 658.0,
    "last_modified": "2020-11-16 22:53:00+00:00"
  }
]
```

Out of Scope
--------------------
- **Bucket Cost Calculation**
  - The implementation is just for the purpose of showing we'd have a calculation going on. 
    It just estimates the storage, not all the costs involved with S3, nor the different prices per region.   
    There's no API or reliable source code to calculate S3 usage available. Also, calculating this in ad-hoc calls is 
    not something very precise. (prices and free tiers change from time to time)    
---    

Ok, why are you not elaborating on this?  
It looks like a lazy job to 110% of the reviewers ;)  

Well, it makes sense to discuss with the team possible solutions before spiking any re-invention of the wheel. Right?

I have a couple of suggestions from the top of my head then:   
1. An enhancement of what AWS offers:
  - Create a real matrix of prices according to the storage type, region, number of requests, I/O traffic, etc., using https://aws.amazon.com/s3/pricing/.
  - Save it in a DynamoDB table, then set a periodic check with CloudWatch to keep up with the prices.  
  - We can also set some storage class metrics in the buckets, which is going to reflect in CloudWatch.
  - Use CloudWatch metrics to get bucket information (same approach I'm using for the Size and Num of objects).
  - Then we apply the cost matrix on top of the metrics to get the total cost of S3.  
2. The one I like :)
  - Use Cost Explorer to identify the cost related to each bucket.
  - We'd need to add a tag to identify each bucket (e.g. "bucket_name" with the name of each bucket as value)
  - Then we'd enable Cost Allocation Tags in the Billing Dashboard and activate the "bucket_name" tag.
  - With this set up we can use an API call to Cost Explorer using the service and bucket_name tag as dimensions and check the current cost of the specific bucket, in total. 
---
 
- Grouping by a region:  
  - Though I have not implemented it, as the response object has the information, we can just transform the data after the process ends.
  
- Size results:
  - Results are in Bytes as CloudWatch sends it by default.
  
- Number of files per Storage Type:
  - This feature hasn't been implemented. We do have the size per storage type though.


  
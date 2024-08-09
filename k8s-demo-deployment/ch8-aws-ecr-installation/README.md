# ECR installation
Use ECR to create a private docker registry

## Create a registry on ECR
![](pics/Pasted%20image%2020240809095332.png)
![](pics/Pasted%20image%2020240809095337.png)


## Install AWS CLI to use commands to upload docker images
- Install AWS CLI on the local PC
	- https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
- Check if the installation is successful
	- `aws --version`


## Create a IAM group and user for AWS CLI
### Creat a group
![](pics/Pasted%20image%2020240809103518.png)
![](pics/Pasted%20image%2020240809103524.png)
![](pics/Pasted%20image%2020240809103529.png)
![](pics/Pasted%20image%2020240809103536.png)

### Create an inline policy for the group 
![](pics/Pasted%20image%2020240809103821.png)
![](pics/Pasted%20image%2020240809103831.png)
![](pics/Pasted%20image%2020240809103840.png)
- Please delete the comments frist
```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Effect": "Allow",
			"Action": "ecr:GetAuthorizationToken",
			"Resource": "*"
		},
        {
            "Effect": "Allow",
            "Action": [
                "ecr:CompleteLayerUpload",
                "ecr:GetAuthorizationToken",
                "ecr:UploadLayerPart",
                "ecr:InitiateLayerUpload",
                "ecr:BatchCheckLayerAvailability",
                "ecr:PutImage"
            ],
            "Resource": "*"
            //"Resource": "arn:aws:ecr:[REGION]:[ACCOUNT_ID]:repository/[REPO_NAME]"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ecr:BatchGetImage",
                "ecr:GetDownloadUrlForLayer"
            ],
            "Resource": "*"
            //"Resource": "arn:aws:ecr:[REGION]:[ACCOUNT_ID]:repository/[REPOSITORY]"
        }
	]
}
```


## Create a user and bind the group to it
![](pics/Pasted%20image%2020240809103908.png)
![](pics/Pasted%20image%2020240809104031.png)

## Create an access key from the IAM user
![](pics/Pasted%20image%2020240809104038.png)
![](pics/Pasted%20image%2020240809104425.png)
![](pics/Pasted%20image%2020240809104438.png)
![](pics/Pasted%20image%2020240809104445.png)
![](pics/Pasted%20image%2020240809104457.png)

## Login to ECR
```bash
# Go to "Amazon ECR">"Private registry">"Repositories">"<your-registry>">"View push commands"
# Get the id from that web page
aws ecr get-login-password --region <region> | \
  sudo docker login \
    --username AWS \
    --password-stdin <ECR-ID>.dkr.ecr.<region>.amazonaws.com
```
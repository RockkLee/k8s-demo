# Push & Pull ECR images
- It seems like each ECR should only include one image with many tags, since there is no image name on the ECR web page.
- However, we can still push multiple images to the ECR by setting the tags as the image names.
```sh
# Each ECR only includes one type of image
docker tag k8s-demo-fastapi:latest 025062954320.dkr.ecr.us-east-1.amazonaws.com/k8s-demo-fastapi:latest
docker push <ecr-id>.dkr.ecr.us-east-1.amazonaws.com/k8s-demo-fastapi:latest

# One ECR includes many types of images
docker tag k8s-demo-fastapi:latest 025062954320.dkr.ecr.us-east-1.amazonaws.com/k8s-demo:fastapi-latest
docker push <ecr-id>.dkr.ecr.us-east-1.amazonaws.com/k8s-demo:fastapi-latest
```

## Push images
- `docker tag <local-image>:<local-image-tag> 025062954320.dkr.ecr.<ecr-region>.amazonaws.com/<ecr-name>:<ecr-tag>`

- `docker push <ecr-id>.dkr.ecr.<ecr-region>.amazonaws.com/<ecr-name>:<ecr-tag>`

## Pull images
- `docker pull <ecr-id>.dkr.ecr.<ecr-region>.amazonaws.com/<ecr-name>:<ecr-tag>`
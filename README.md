# K8s CI/CD using Jenkins-CloudFormation

Here, we are deploying EKS cluster using CloudFormation templates. After cluster is setup we will deploy our Flask app on that cluster using Jenkins.
We can also update the web app using Jenkins by doing a Rolling deployment of Kubernetes.

## CloudFormation

CloudFormation templates are in `/infra` folder.

- First deploy network.yml to setup VPC and subnets for the cluster. The stack name used here is `capstone network`.

- Then create a stack `capstone-cluster` for EKS cluster by deploying `cluster.yml`.

- Now, final stack `node.yml` is to be deployed to setup worker nodes of EKS.

Sample command to deploy cloudformation stack

```bash
aws cloudformation create-stack --stack-name capstone-cluster --template-body file://cluster.yml --region us-east-1 --capabilities CAPABILITY_NAMED_IAM
```

> If you use the above command and deploy from Jenkins, you will same some steps to whitelist your Jenkins role on EKS cluster i.e basically updating EKS cluster's configmap step will be saved.

## Jenkins

When you are done with infra setup, now you should connect EKS cluster in Jenkins by following [these](https://aws.amazon.com/premiumsupport/knowledge-center/eks-cluster-connection/) steps.

After doing that setup AWS plugin and Docker credentials.
Then connect BlueOcean to your github repository. Done!

## WebApp

The webapp is a simple visit counter app which used flask as backend and the visit data is stored inside redis.
the flack code is part of frontend folder and redis component is in backend folder.
Whenever a user visits page, flask app will get called and will update the count in redis.

For ease architecture, currently both kubernetes service use LoadBalancer to commumnicate.

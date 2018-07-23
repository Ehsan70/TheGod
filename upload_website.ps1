
param (
    [Parameter(Mandatory=$true)]
    [string]$S3Bucket = ""
)


if ([string]::IsNullOrEmpty($S3Bucket)){
     throw "S3 bucket have to be specified."
}

aws s3 cp ./website/ "s3://$S3Bucket" --recursive --exclude "*.yaml" --exclude "*.md"
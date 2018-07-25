
param (
    [Parameter(Mandatory=$true)]
    [string]$S3Bucket = "",
    [string]$AwsProfile = ""
)


if ([string]::IsNullOrEmpty($S3Bucket)){
     throw "S3 bucket have to be specified."
}

if ([string]::IsNullOrEmpty($AwsProfile)){
    Write-Host "The default profile will be used."
    aws s3 cp ./website/ "s3://$S3Bucket" --recursive --exclude "*.yaml" --exclude "*.md"
}else{
    aws s3 cp ./website/ "s3://$S3Bucket" --recursive --exclude "*.yaml" --exclude "*.md" --profile "$AwsProfile"
}


$token  = $env:GITHUB_TOKEN

$headers = @{ Authorization = "token $token" }

Invoke-RestMethod `
  -Uri "https://api.github.com/user/repos" `
  -Headers $headers `
  -Method Post `
  -Body '{"name":"DSA-MASTERY-JOURNEY","private":false}' `
  -ContentType "application/json"
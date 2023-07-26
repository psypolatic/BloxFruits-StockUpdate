local HttpService = game:GetService('HttpService')
local HttpRequest = (syn and syn.request) or http and http.request or http_request or (fluxus and fluxus.request) or request
local Players = game:GetService('Players')


--Change Me
local player = Players:WaitForChild('Yourusername')



local playerGui = player:WaitForChild('PlayerGui')
local main = playerGui:WaitForChild('Main')
local fruitShop = main:WaitForChild('FruitShop')
local left = fruitShop:WaitForChild('Left')
local center = left:WaitForChild('Center')
local scrollingFrame = center:WaitForChild('ScrollingFrame')
local container = scrollingFrame:WaitForChild('Container')

local prices = {}

for i, child in ipairs(container:GetChildren()) do
    if child:IsA('Frame') and child:FindFirstChild('Price') then
        local price = child.Price
        local text = price.Text

        prices[child.Name] = text
    end
end

local jsonPrices = HttpService:JSONEncode(prices)

local response = HttpRequest(
    {
      --Change me
        Url = "YourServer.com",
        Method = "POST",
        Headers = {
            ["Content-Type"] = "application/json"
        },
        Body = jsonPrices
    }
)

for i,v in pairs(response) do
   print(i,v)
end

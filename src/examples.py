# login
import vk_user
vkUserClient = vk_user.VkUserClient(access_token="")
print(f"-- Account user_id is::: {vkUserClient.user_id}")

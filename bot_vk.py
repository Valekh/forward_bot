import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk_session = vk_api.VkApi(token='vk1.a.B_NzeFa7gietZFkQJv57KMwRl_blfmUy4774wE9qnIINqT-l0H_v0ho8TMYxiHWwM0VcR55DGfma85pHy3AYotxnsrt8fb1RriaxX1WAgIj1rpXhbdzfGVD-L25j-8NFlHh2-ur9tgkRJLZoZuicg0oos_cxh1RW1xk0shd1itY5GzPbG8Kwoi4irGGtR60vwA6_Nma9kpM_bDmXZI5uOQ')
group_id = '217268312'
longpoll = VkBotLongPoll(vk_session, group_id)


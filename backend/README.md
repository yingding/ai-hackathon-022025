# Introduction

## On windows 11
1. copy the `.env.example` to `.env` and fill in your azure credentials

2. Activate the venv
```powershell
$VERSION="3.13";
$ENV_NAME="multiagents";
$ENV_SURFIX="pip";
$ENV_FULL_NAME = "$ENV_NAME$VERSION$ENV_SURFIX";
$WORK_DIR="$env:USERPROFILE\Documents\VENV\";
& "$WORK_DIR$ENV_FULL_NAME\Scripts\Activate.ps1";
Invoke-Expression "(Get-Command python).Source";
```

3. change directory to the project playground
```powershell
$PROJ_DIR_NAME="ai-hackathon-022025\backend";
$PROJ_ROOT_DIRS="Documents\VCS\events";
$PROJ_PATH="$env:USERPROFILE\$PROJ_ROOT_DIRS\$PROJ_DIR_NAME";
cd "$PROJ_PATH";

& "python" main.py
```

4. testing the swagger api
```
http://localhost:8000/docs
```

**Single Agent**:

```shell
curl -X 'POST' \
  'http://localhost:8000/agent/chat' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "message": "What are some innovative approaches to reduce plastic waste in urban environments?",
  "system_prompt": "You are a helpful assistant that provides concise and accurate information.",
  "temperature": 0.7,
  "available_plugins": [],
  "chat_history": []
}'
```

Using the swagger UI
```json
{
  "message": "What are some innovative approaches to reduce plastic waste in urban environments?",
  "system_prompt": "You are a helpful assistant that provides concise and accurate information.",
  "temperature": 0.7,
  "available_plugins": [],
  "chat_history": []
}
```

<!--
output:
```json
{
  "response": {
    "ai_model_id": "gpt-4o-mini",
    "metadata": {
      "logprobs": null,
      "id": "chatcmpl-BRREEcDfBG71jgshCzDZEoJdFwlFo",
      "created": 1745879222,
      "system_fingerprint": "fp_ded0d14823",
      "usage": {
        "prompt_tokens": 188,
        "completion_tokens": 347
      }
    },
    "content_type": "message",
    "role": "assistant",
    "name": "PlaygroundAgent",
    "items": [
      {
        "ai_model_id": null,
        "metadata": {},
        "content_type": "text",
        "text": "Here are some innovative approaches to reduce plastic waste in urban environments:\n\n1. **Plastic Waste Collection Apps**: Develop mobile applications that incentivize residents to collect plastic waste. Users can earn rewards or points that can be redeemed for local services.\n\n2. **Community Recycling Hubs**: Establish local recycling centers where residents can bring their plastics, along with educational programs on proper disposal and recycling practices.\n\n3. **Biodegradable Alternatives**: Promote the use of biodegradable materials as alternatives to traditional plastics, especially in packaging and single-use items.\n\n4. **Plastic Credit Systems**: Implement a system where companies can purchase 'plastic credits' by funding clean-up initiatives or developing sustainable packing technologies.\n\n5. **Upcycling Workshops**: Organize community workshops that teach residents how to upcycle plastic waste into usable products, thereby extending the life cycle of plastic materials.\n\n6. **Ban on Single-use Plastics**: Enforce regulations that ban or limit single-use plastics, encouraging businesses to adopt more sustainable practices.\n\n7. **Circular Economy Initiatives**: Foster partnerships between waste management companies and local businesses to implement a circular economy model focusing on recycling and reusing materials.\n\n8. **Plastic Footprints**: Allow individuals and companies to track their plastic usage and waste through mobile platforms, promoting accountability and encouraging reductions in consumption.\n\n9. **Smart Waste Bins**: Utilize smart waste bin technology that detects and sorts plastic waste automatically, making recycling more efficient.\n\n10. **Urban Green Solutions**: Develop urban green spaces that incorporate plastic waste as part of art installations or landscaping materials, thereby highlighting the issue while beautifying the environment.\n\nImplementing a combination of these approaches can significantly contribute to reducing plastic waste in urban settings.",
        "encoding": null
      }
    ],
    "encoding": null,
    "finish_reason": "stop",
    "status": null
  },
  "chat_history": [
    {
      "role": "user",
      "content": "What are some innovative approaches to reduce plastic waste in urban environments?"
    },
    {
      "role": "assistant",
      "content": {
        "ai_model_id": "gpt-4o-mini",
        "metadata": {
          "logprobs": null,
          "id": "chatcmpl-BRREEcDfBG71jgshCzDZEoJdFwlFo",
          "created": 1745879222,
          "system_fingerprint": "fp_ded0d14823",
          "usage": {
            "prompt_tokens": 188,
            "completion_tokens": 347
          }
        },
        "content_type": "message",
        "role": "assistant",
        "name": "PlaygroundAgent",
        "items": [
          {
            "ai_model_id": null,
            "metadata": {},
            "content_type": "text",
            "text": "Here are some innovative approaches to reduce plastic waste in urban environments:\n\n1. **Plastic Waste Collection Apps**: Develop mobile applications that incentivize residents to collect plastic waste. Users can earn rewards or points that can be redeemed for local services.\n\n2. **Community Recycling Hubs**: Establish local recycling centers where residents can bring their plastics, along with educational programs on proper disposal and recycling practices.\n\n3. **Biodegradable Alternatives**: Promote the use of biodegradable materials as alternatives to traditional plastics, especially in packaging and single-use items.\n\n4. **Plastic Credit Systems**: Implement a system where companies can purchase 'plastic credits' by funding clean-up initiatives or developing sustainable packing technologies.\n\n5. **Upcycling Workshops**: Organize community workshops that teach residents how to upcycle plastic waste into usable products, thereby extending the life cycle of plastic materials.\n\n6. **Ban on Single-use Plastics**: Enforce regulations that ban or limit single-use plastics, encouraging businesses to adopt more sustainable practices.\n\n7. **Circular Economy Initiatives**: Foster partnerships between waste management companies and local businesses to implement a circular economy model focusing on recycling and reusing materials.\n\n8. **Plastic Footprints**: Allow individuals and companies to track their plastic usage and waste through mobile platforms, promoting accountability and encouraging reductions in consumption.\n\n9. **Smart Waste Bins**: Utilize smart waste bin technology that detects and sorts plastic waste automatically, making recycling more efficient.\n\n10. **Urban Green Solutions**: Develop urban green spaces that incorporate plastic waste as part of art installations or landscaping materials, thereby highlighting the issue while beautifying the environment.\n\nImplementing a combination of these approaches can significantly contribute to reducing plastic waste in urban settings.",
            "encoding": null
          }
        ],
        "encoding": null,
        "finish_reason": "stop",
        "status": null
      }
    }
  ],
  "plugin_calls": []
}
```
-->

**Multi Agent**:

```shell
curl -X 'POST' \
  'http://localhost:8000/agent/multi-chat' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "message": "What are some innovative approaches to reduce plastic waste in urban environments?",
  "system_prompt": "You are a helpful assistant that provides concise and accurate information.",
  "temperature": 0.7,
  "available_plugins": [],
  "chat_history": [],
  "agent_configs": [],
  "max_iterations": 4
}'
```

Using the swagger UI
```json
{
  "message": "What are some innovative approaches to reduce plastic waste in urban environments?",
  "system_prompt": "You are a helpful assistant that provides concise and accurate information.",
  "temperature": 0.7,
  "available_plugins": [],
  "chat_history": [],
  "agent_configs": [],
  "max_iterations": 4
}
```

<!--
Output:
```json
{
  "agent_responses": [
    {
      "agent_name": "Researcher",
      "content": "Innovative approaches to reduce plastic waste in urban environments include:\n\n1. **Zero Waste Initiatives**: Cities like San Francisco have implemented comprehensive zero waste programs, encouraging recycling and composting to minimize waste.\n\n2. **Community-Based Programs**: Engaging local communities in clean-up drives, recycling education, and the promotion of reusable products can foster collective responsibility.\n\n3. **Plastic Bans and Fees**: Cities such as Seattle and Dublin have enacted bans on single-use plastics like straws and bags or have introduced fees for their use to encourage alternatives.\n\n4. **Smart Waste Management**: Utilizing technology, such as IoT sensors in bins to monitor waste levels, can optimize collection routes and reduce overflow.\n\n5. **Incentivizing Businesses**: Offering incentives or recognition programs for businesses that adopt sustainable practices or reduce plastic usage can drive change.\n\n6. **Innovative Recycling Technologies**: Urban areas can invest in advanced recycling facilities that can handle different types of plastics more effectively, such as chemical recycling methods.\n\n7. **Education and Awareness Campaigns**: Running campaigns to educate the public about the impacts of plastic waste and promoting the use of sustainable alternatives.\n\n8. **Partnerships with Nonprofits**: Collaborating with organizations focused on environmental sustainability can facilitate clean-up initiatives and foster innovation in waste management solutions.\n\n9. **Urban Planning and Design**: Designing cities with sustainability in mind, such as incorporating green spaces and waste-to-energy facilities, can help minimize plastic use.\n\nThese strategies, when implemented, can contribute significantly to reducing plastic waste in urban settings.",
      "is_new": true
    },
    {
      "agent_name": "Innovator",
      "content": "Innovative approaches to reducing plastic waste in urban environments include:\n\n1. **Circular Economy Models**: Shift from linear to circular systems where waste is reprocessed into new products, promoting a sustainable lifecycle for materials.\n\n2. **Pop-Up Refill Stations**: Establish temporary refill points for everyday products (e.g., toiletries, cleaning supplies) to encourage using reusable containers.\n\n3. **Extended Producer Responsibility (EPR)**: Mandate manufacturers to take back products at the end of their life, incentivizing them to create less wasteful designs.\n\n4. **Plastic-Free Zones**: Designate specific areas within cities as plastic-free, promoting local shops and restaurants that don’t use plastic packaging.\n\n5. **Creative Upcycling Workshops**: Organize community events where individuals learn to upcycle plastic waste into functional items, fostering creativity and awareness.\n\n6. **Blockchain for Recycling**: Implement blockchain technology to track plastic waste disposal, rewarding individuals and businesses for proper recycling practices.\n\n7. **Sustainable Transport Solutions**: Promote the use of bicycle-sharing programs and electric public transport to reduce reliance on plastic-heavy gasoline vehicles.\n\n8. **Public Art Installations**: Use plastic waste to create stunning art pieces in public spaces, raising awareness while beautifying urban areas.\n\n9. **Plastic Footprint Challenge**: Launch citywide challenges encouraging residents to reduce their plastic use, with rewards for those who significantly cut down their plastic footprint.\n\nBy combining these strategies, urban environments can significantly reduce plastic waste while fostering community involvement and environmental stewardship.",
      "is_new": true
    },
    {
      "agent_name": "Critic",
      "content": "While these innovative approaches to reducing plastic waste in urban environments are commendable, some strengths and weaknesses can be identified.\n\n### Strengths:\n1. **Community Engagement**: Many strategies such as upcycling workshops and challenges actively involve the community, fostering a sense of shared responsibility.\n2. **Versatile Solutions**: The approaches cater to different sectors: consumers, businesses, and municipalities, promoting widespread impact.\n3. **Technology Integration**: Using tech solutions like blockchain for recycling can enhance transparency and efficiency in waste management.\n4. **Creativity and Awareness**: Art installations and workshops can effectively raise awareness about plastic waste in an engaging manner.\n\n### Weaknesses:\n1. **Implementation and Enforcement**: Strategies like EPR and plastic-free zones require strong regulatory frameworks and enforcement, which can be challenging.\n2. **Equity Issues**: Programs may inadvertently overlook low-income communities, who may lack access to refill stations or sustainable alternatives.\n3. **Sustainability of Initiatives**: Pop-up stations and workshops may face sustainability challenges if they lack ongoing funding or volunteer support.\n4. **Behavior Change Resistance**: Encouraging shifts in consumer behavior can be difficult; residents may resist changes to convenience or habits.\n\n### Suggested Improvements:\n1. **Tailored Outreach**: Ensure that educational campaigns address the needs of diverse community groups, including marginalized populations.\n2. **Partnerships with Local Businesses**: Collaborate with businesses to provide incentives for participation in sustainable practices, enhancing the local economy.\n3. **Long-term Funding Models**: Develop and secure sustainable funding sources for initiatives to ensure consistency and growth.\n4. **Pilot Programs**: Test processes on a small scale before citywide implementation to identify obstacles and refine strategies.\n\nBy addressing these weaknesses and implementing suggested improvements, urban areas can create more robust and effective strategies to reduce plastic waste.",
      "is_new": true
    },
    {
      "agent_name": "Synthesizer",
      "content": "In summary, effective strategies for reducing plastic waste in urban environments can be synthesized into a balanced perspective that highlights both innovation and critical considerations:\n\n### Common Themes:\n1. **Community Engagement**: Strategies such as workshops, clean-up events, and challenges promote active participation and shared responsibility among residents.\n   \n2. **Regulatory Support**: Initiatives like EPR, plastic bans, and designated plastic-free zones require strong regulatory frameworks to ensure compliance and effectiveness.\n\n3. **Technology Utilization**: Integrating technology (e.g., smart waste management and blockchain) enhances efficiency, transparency, and tracking of waste.\n\n4. **Education and Awareness**: Public campaigns and creative arts can effectively inform and motivate urban populations towards sustainable practices.\n\n5. **Collaboration**: Partnerships with local businesses and nonprofits can amplify the impact and sustainability of initiatives.\n\n### Critical Considerations:\n- **Equity Issues**: Strategies need to ensure accessibility for all community segments, particularly marginalized groups.\n  \n- **Sustainability**: Long-term funding and support are vital to maintain initiatives and prevent them from being short-lived.\n\n- **Behavior Change**: Overcoming resistance to new habits will be necessary for successful implementation; tailored approaches may be required.\n\nBy integrating these insights, urban environments can adopt innovative and robust strategies that not only effectively reduce plastic waste but also promote community involvement and environmental sustainability.",
      "is_new": true
    }
  ],
  "chat_history": [
    {
      "role": "user",
      "content": "What are some innovative approaches to reduce plastic waste in urban environments?"
    },
    {
      "role": "assistant",
      "content": "Innovative approaches to reduce plastic waste in urban environments include:\n\n1. **Zero Waste Initiatives**: Cities like San Francisco have implemented comprehensive zero waste programs, encouraging recycling and composting to minimize waste.\n\n2. **Community-Based Programs**: Engaging local communities in clean-up drives, recycling education, and the promotion of reusable products can foster collective responsibility.\n\n3. **Plastic Bans and Fees**: Cities such as Seattle and Dublin have enacted bans on single-use plastics like straws and bags or have introduced fees for their use to encourage alternatives.\n\n4. **Smart Waste Management**: Utilizing technology, such as IoT sensors in bins to monitor waste levels, can optimize collection routes and reduce overflow.\n\n5. **Incentivizing Businesses**: Offering incentives or recognition programs for businesses that adopt sustainable practices or reduce plastic usage can drive change.\n\n6. **Innovative Recycling Technologies**: Urban areas can invest in advanced recycling facilities that can handle different types of plastics more effectively, such as chemical recycling methods.\n\n7. **Education and Awareness Campaigns**: Running campaigns to educate the public about the impacts of plastic waste and promoting the use of sustainable alternatives.\n\n8. **Partnerships with Nonprofits**: Collaborating with organizations focused on environmental sustainability can facilitate clean-up initiatives and foster innovation in waste management solutions.\n\n9. **Urban Planning and Design**: Designing cities with sustainability in mind, such as incorporating green spaces and waste-to-energy facilities, can help minimize plastic use.\n\nThese strategies, when implemented, can contribute significantly to reducing plastic waste in urban settings.",
      "agent_name": "Researcher"
    },
    {
      "role": "assistant",
      "content": "Innovative approaches to reducing plastic waste in urban environments include:\n\n1. **Circular Economy Models**: Shift from linear to circular systems where waste is reprocessed into new products, promoting a sustainable lifecycle for materials.\n\n2. **Pop-Up Refill Stations**: Establish temporary refill points for everyday products (e.g., toiletries, cleaning supplies) to encourage using reusable containers.\n\n3. **Extended Producer Responsibility (EPR)**: Mandate manufacturers to take back products at the end of their life, incentivizing them to create less wasteful designs.\n\n4. **Plastic-Free Zones**: Designate specific areas within cities as plastic-free, promoting local shops and restaurants that don’t use plastic packaging.\n\n5. **Creative Upcycling Workshops**: Organize community events where individuals learn to upcycle plastic waste into functional items, fostering creativity and awareness.\n\n6. **Blockchain for Recycling**: Implement blockchain technology to track plastic waste disposal, rewarding individuals and businesses for proper recycling practices.\n\n7. **Sustainable Transport Solutions**: Promote the use of bicycle-sharing programs and electric public transport to reduce reliance on plastic-heavy gasoline vehicles.\n\n8. **Public Art Installations**: Use plastic waste to create stunning art pieces in public spaces, raising awareness while beautifying urban areas.\n\n9. **Plastic Footprint Challenge**: Launch citywide challenges encouraging residents to reduce their plastic use, with rewards for those who significantly cut down their plastic footprint.\n\nBy combining these strategies, urban environments can significantly reduce plastic waste while fostering community involvement and environmental stewardship.",
      "agent_name": "Innovator"
    },
    {
      "role": "assistant",
      "content": "While these innovative approaches to reducing plastic waste in urban environments are commendable, some strengths and weaknesses can be identified.\n\n### Strengths:\n1. **Community Engagement**: Many strategies such as upcycling workshops and challenges actively involve the community, fostering a sense of shared responsibility.\n2. **Versatile Solutions**: The approaches cater to different sectors: consumers, businesses, and municipalities, promoting widespread impact.\n3. **Technology Integration**: Using tech solutions like blockchain for recycling can enhance transparency and efficiency in waste management.\n4. **Creativity and Awareness**: Art installations and workshops can effectively raise awareness about plastic waste in an engaging manner.\n\n### Weaknesses:\n1. **Implementation and Enforcement**: Strategies like EPR and plastic-free zones require strong regulatory frameworks and enforcement, which can be challenging.\n2. **Equity Issues**: Programs may inadvertently overlook low-income communities, who may lack access to refill stations or sustainable alternatives.\n3. **Sustainability of Initiatives**: Pop-up stations and workshops may face sustainability challenges if they lack ongoing funding or volunteer support.\n4. **Behavior Change Resistance**: Encouraging shifts in consumer behavior can be difficult; residents may resist changes to convenience or habits.\n\n### Suggested Improvements:\n1. **Tailored Outreach**: Ensure that educational campaigns address the needs of diverse community groups, including marginalized populations.\n2. **Partnerships with Local Businesses**: Collaborate with businesses to provide incentives for participation in sustainable practices, enhancing the local economy.\n3. **Long-term Funding Models**: Develop and secure sustainable funding sources for initiatives to ensure consistency and growth.\n4. **Pilot Programs**: Test processes on a small scale before citywide implementation to identify obstacles and refine strategies.\n\nBy addressing these weaknesses and implementing suggested improvements, urban areas can create more robust and effective strategies to reduce plastic waste.",
      "agent_name": "Critic"
    },
    {
      "role": "assistant",
      "content": "In summary, effective strategies for reducing plastic waste in urban environments can be synthesized into a balanced perspective that highlights both innovation and critical considerations:\n\n### Common Themes:\n1. **Community Engagement**: Strategies such as workshops, clean-up events, and challenges promote active participation and shared responsibility among residents.\n   \n2. **Regulatory Support**: Initiatives like EPR, plastic bans, and designated plastic-free zones require strong regulatory frameworks to ensure compliance and effectiveness.\n\n3. **Technology Utilization**: Integrating technology (e.g., smart waste management and blockchain) enhances efficiency, transparency, and tracking of waste.\n\n4. **Education and Awareness**: Public campaigns and creative arts can effectively inform and motivate urban populations towards sustainable practices.\n\n5. **Collaboration**: Partnerships with local businesses and nonprofits can amplify the impact and sustainability of initiatives.\n\n### Critical Considerations:\n- **Equity Issues**: Strategies need to ensure accessibility for all community segments, particularly marginalized groups.\n  \n- **Sustainability**: Long-term funding and support are vital to maintain initiatives and prevent them from being short-lived.\n\n- **Behavior Change**: Overcoming resistance to new habits will be necessary for successful implementation; tailored approaches may be required.\n\nBy integrating these insights, urban environments can adopt innovative and robust strategies that not only effectively reduce plastic waste but also promote community involvement and environmental sustainability.",
      "agent_name": "Synthesizer"
    }
  ],
  "plugin_calls": []
}
```
-->
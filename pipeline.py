from agents import build_search_agent, build_reader_agent, writer_chain, critic_chain

def run_research_pipeline(topic : str) -> dict :
    state = {}

    #step 1 - search agent working
    print("\n "+" ="*50)
    print("step 1 - search agent is working ...")
    print("="*50)

    search_agent=build_search_agent()
    search_result=search_agent.invoke({
        "messages": [("user",f"You MUST use the web_search tool to find recent, reliable and detailed information about : {topic}. Do not answer from your own knowledge. In your final response, you MUST include the exact URLs you found.")]
    })

    state["search_results"]=search_result["messages"][-1].content

    print("\n search result \n",state['search_results'])

    #step 2 - reader agent working
    print("\n " + " ="*50)
    print("step 2 - reader agent is working ...")
    print("="*50)

    reader_agent=build_reader_agent()
    reader_result=reader_agent.invoke({
        "messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and you MUST use the scrape_url tool to scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_results'][:2000]}"
        )]
    })

    state['scraped_content'] = reader_result['messages'][-1].content

    print("\n scraped content \n",state['scraped_content'])
    
    
    #step 3 - writer chain working
    print("\n " + " ="*50)
    print("step 3 - writer chain is working ...")
    print("="*50)

    research_combined=(
        f"SEARCH RESULTS : \n {state['search_results']} \n\n"
        f"DETAILED SCRAPED CONTENT : \n {state['scraped_content']}"
    )
    
    state["report"]=writer_chain.invoke({
        "topic":topic,
        "research":research_combined
    })

    print("\n Final Report \n",state['report'])

    #step 4 - critic chain working
    print("\n " + " ="*50)
    print("step 4 - critic chain is working ...")
    print("="*50)

    state['feedback']=critic_chain.invoke({
        "report":state['report']
    })

    print("\n Critic Report \n",state['feedback'])

    return state
    
if __name__ == "__main__":
    topic =input("\n Enter a research topic : ")
    run_research_pipeline(topic)
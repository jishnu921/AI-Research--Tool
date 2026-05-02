from agents import writer_chain, critic_chain, llm


def run_research_pipeline(topic: str) -> dict:

    state = {}

    # ================= STEP 1 =================
    print("\n" + "=" * 50)
    print("step 1 - search agent is working ...")
    print("=" * 50)

    response = llm.invoke(
        f"""
Answer in EXACTLY 3 lines.

Topic: {topic}

Rules:
- No disclaimers
- No extra explanation
- No examples
- Only 3 lines
"""
    )

    state["search_results"] = response.content

    print("\n search result:\n", state["search_results"])

    # ================= STEP 2 =================
    print("\n" + "=" * 50)
    print("step 2 - expanding research ...")
    print("=" * 50)

    state["scraped_content"] = llm.invoke(
        f"""
Expand this into clear bullet points.

Content:
{state["search_results"]}

Rules:
- No unrelated topics
- No puzzles
- Stay factual
"""
    ).content

    print("\n scraped content:\n", state["scraped_content"])

    # ================= STEP 3 =================
    print("\n" + "=" * 50)
    print("step 3 - Writer is drafting the report ...")
    print("=" * 50)

    research_combined = (
        f"SEARCH RESULTS:\n{state['search_results']}\n\n"
        f"DETAILED CONTENT:\n{state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    print("\n Final Report\n", state["report"])

    # ================= STEP 4 =================
    print("\n" + "=" * 50)
    print("step 4 - critic is reviewing the report")
    print("=" * 50)

    state["feedback"] = critic_chain.invoke({
        "report": state["report"]
    })

    print("\n critic report\n", state["feedback"])

    return state


if __name__ == "__main__":
    topic = input("\n Enter a research topic: ")
    run_research_pipeline(topic)
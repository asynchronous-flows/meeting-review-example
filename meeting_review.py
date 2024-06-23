from asyncflows import AsyncFlows


async def main():
    # Load the flow from the file and set the variable
    flow = AsyncFlows.from_file("meeting_review.yaml")

    # Read `meeting_notes.txt` and set the variable
    with open("meeting_notes.txt") as f:
        meeting_notes = f.read()
    flow = flow.set_vars(
        meeting_notes=meeting_notes,
    )

    # Run the flow
    result = await flow.run('structure.data')

    # Print the action items
    print(result['action_items'])


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())

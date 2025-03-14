import argparse
import pubmed_fetcher


def main():
    parser = argparse.ArgumentParser(
        description="Fetch PubMed papers related to a query.")
    parser.add_argument("query", help="Search query for PubMed")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="Enable debug mode")
    parser.add_argument("-f", "--file", type=str,
                        help="Specify filename to save results (default: print to console)")

    args = parser.parse_args()

    papers = pubmed_fetcher.fetch_pubmed_papers(args.query)

    if not papers:
        print("No qualifying papers found.")
        return

    if args.file:
        pubmed_fetcher.save_to_csv(papers, args.file)
    else:
        if args.debug:
             print(f"Debug: Searching for '{args.query}'")
             print(f"Debug: Searching completed and fetching papers.")
        for paper in papers:
            print(paper)
        if args.debug:
             print(f"Debug:'{args.query}' has been successfully fetched.")

if __name__ == "__main__":
    main()

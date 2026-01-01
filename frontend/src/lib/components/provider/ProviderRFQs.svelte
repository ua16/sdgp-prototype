<script lang="ts">
    async function getRFQs() {
        try {
            const response = await fetch("http://127.0.0.1:5000/rfqs");
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            // Parse JSON array directly
            const rfqs = await response.json();
            return rfqs;
        } catch (err) {
            console.error("Error fetching RFQs:", err);
            return [];
        }
    }

    let quotationsInfo = getRFQs();
</script>

<div class="w-full h-full">
    <!-- Maybe refactor this to a separate thing so we have a way of always having a sign in -->
    <div
        class="text-black font-bold border-b-3 border-stone-300 bg-stone-100 p-2"
    >
        Dashboard
    </div>
    <div class="grid place-items-center bg-stone-200 pt-8">
        <div class="flex flex-col text-black -full ml-2 gap-4">
            <div class="flex flex-row gap-2 items-center">
                <div class="flex flex-col">
                    <div class="font-bold text-xl">Requests for Quotations</div>
                    <div>
                        Browse and respond to RFQs sent by shippers relevant to
                        your service categories.
                    </div>
                </div>

                <input
                    class="rounded-full max-h-7 bg-stone-100"
                    type="text"
                    placeholder="Search"
                />
                <button
                    class="max-h-7 rounded-full bg-stone-100 hover:bg-stone-200 pl-2 pr-2"
                >
                    Sort
                </button>
                <button
                    class="max-h-7 rounded-full bg-stone-100 hover:bg-stone-200 pl-2 pr-2"
                >
                    Filter
                </button>
                <button
                    class="max-h-7 rounded-full bg-stone-100 hover:bg-stone-200 pl-2 pr-2"
                    >:</button
                >
            </div>
        </div>

        <table class="w-9/10 mt-8 mb-8 table-auto rounded-lg">
            <thead class="h-10 bg-stone-300">
                <tr class="text-black rounded-t-2xl">
                    <th>RFQ ID</th>
                    <th>Shipper</th>
                    <th>Required Services</th>
                    <th>Origin+Destination</th>
                    <th>Date Created</th>
                    <th>Deadline</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody class="bg-stone-100 text-black text-center">
                {#await quotationsInfo}
                    <tr>
                        <td colspan="7">Loading...</td>
                    </tr>
                {:then data}
                    {#each data as q}
                        <tr>
                            <td>{q.ident}</td>
                            <td>{q.Shipper}</td>
                            <td>{q.RequiredServices}</td>
                            <td>{q.OriginDestination}</td>
                            <td>{q.DateCreated}</td>
                            <td>{q.Deadline}</td>
                            <td>{q.Status}</td>
                        </tr>
                    {/each}
                {:catch error}
                    <tr>
                        <td colspan="7">Error loading data: {error.message}</td>
                    </tr>
                {/await}
            </tbody>
        </table>
    </div>
</div>

<style>
    thead tr:first-child th:first-child {
        border-top-left-radius: 0.5rem;
    }

    thead tr:first-child th:last-child {
        border-top-right-radius: 0.5rem;
    }

    td {
        padding-top: 10px;
        padding-bottom: 10px;
        border-bottom: 1px solid oklch(86.9% 0.005 56.366);
    }
</style>

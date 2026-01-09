<script lang="ts">
    function clamp(val: number, vmin: number, vmax: number) {
        if (val < vmin) {
            return vmin;
        } else if (val > vmax) {
            return vmax;
        } else {
            return val;
        }
    }

    let rfqslen = 0;
    async function getRFQs(targetOrgId: number) {
        const apiKey = "your-api-key-here";

        const response = await fetch("http://localhost:5000/rfqs", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-API-Key": apiKey,
            },
            body: JSON.stringify({ targetOrgId }),
        });

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const rfqs = await response.json(); // <- saved to variable
        rfqslen = rfqs.length;

        return rfqs;
    }

    const orgID = 1;
    let quotationsInfo: Promise<any[]> = getRFQs(orgID);

    let firstQuoteStart = $state(0);
    let quoteStepSize = 8;
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
                    {#each Array(quoteStepSize) as _, i}
                        {#if i + firstQuoteStart < rfqslen}
                            <tr>
                                <td>{data[i + firstQuoteStart].rfqid}</td>
                                <td>{data[i + firstQuoteStart].companyName}</td
                                >
                                <td>Freight</td>
                                <td>{data[i + firstQuoteStart].origin} > {data[i + firstQuoteStart].destination}</td>
                                <td>{data[i + firstQuoteStart].creationDate}</td
                                >
                                <td>{data[i + firstQuoteStart].expiryDate}</td>
                                <td>Pending</td>
                            </tr>
                        {/if}
                    {/each}
                {:catch error}
                    <tr>
                        <td colspan="7">Error loading data: {error.message}</td>
                    </tr>
                {/await}
            </tbody>
        </table>

        <div class="p-10 text-black flex flex-row gap-3">
            <button
                onclick={() => {
                    firstQuoteStart -= quoteStepSize;
                    firstQuoteStart = clamp(
                        firstQuoteStart,
                        0,
                        rfqslen - quoteStepSize,
                    );
                }}
                class="rounded-full bg-stone-300 pl-10 pr-10">-</button
            >
            <button
                onclick={() => {
                    firstQuoteStart += quoteStepSize;
                    firstQuoteStart = clamp(
                        firstQuoteStart,
                        0,
                        rfqslen - quoteStepSize,
                    );
                }}
                class="rounded-full bg-stone-300 pl-10 pr-10">+</button
            >
            <span>{firstQuoteStart}</span>
        </div>
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

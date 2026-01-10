<script lang="ts">
    let { rfqid } = $props();

    async function getRFQ(targetOrgId: number, targetRfq: number) {
        const apiKey = "your-api-key-here";

        const response = await fetch("http://localhost:5000/get-single-rfq", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-API-Key": apiKey,
            },
            body: JSON.stringify({ targetOrgId, targetRfq }),
        });

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const rfq = await response.json();
        return rfq[0];
    }

    let orgID = 1;
    let quotationInfo: Promise<any> = getRFQ(orgID, rfqid);

    // Imports

    import CargoInfo from "./applets/smores/CargoInfo.svelte";
    import ShipmentRoute from "./applets/smores/ShipmentRoute.svelte";
    import ShipperDetails from "./applets/smores/ShipperDetails.svelte";
    import Timeline from "./applets/smores/Timeline.svelte";
    import ServiceRequirements from "./applets/smores/ServiceRequirements.svelte";
    import SpecialInstructions from "./applets/smores/SpecialInstructions.svelte";
</script>

<div class="w-full h-screen overflow-y-auto">
    <div
        class="text-black font-bold border-b-3 border-stone-300 bg-stone-100 p-2"
    >
        RFQ > {rfqid}
    </div>
    <div class="grid place-items-center bg-stone-200 pt-8">
        {#await quotationInfo}
            <div>Loading Quotation</div>
        {:then data}
            <div class="flex flex-row gap-2 w-8/10 mb-5">
                <!-- Cargo Info stuff -->
                <div class="w-1/2 flex flex-col gap-2">
                    <ShipmentRoute quotedata={data} />
                    <CargoInfo quotedata={data} />
                    <ServiceRequirements quotedata={data} />
                    <SpecialInstructions quotedata={data} />
                </div>

                <!-- Shipper detail stuff -->
                <div class="w-1/2 flex flex-col gap-2">
                    <ShipperDetails quotedata={data} />
                    <Timeline quotedata={data} />
                </div>
            </div>
        {/await}
    </div>
</div>

<script>
    import ActiveRFQs from "./applets/marshmallows/ActiveRFQs.svelte";
    import MonthlyRevenue from "./applets/graphs/MonthlyRevenue.svelte";
    import ServiceDistribution from "./applets/graphs/ServiceDistribution.svelte";
</script>

<div class="w-full h-full">
    <!-- Maybe refactor this to a separate thing so we have a way of always having a sign in -->
    <div class="text-black font-bold border-b-3 border-stone-300 bg-stone-100 p-2">
        Dashboard
    </div>
    <div class="grid place-items-center bg-stone-200">
        <!-- All the stuff is contained in this -->
        <div class="grid w-9/10 gap-2 bg-stone-200">
            <div class="text-black">Good Day James</div>
            <!-- TODO : Maybe move this to another container at some point -->
            <div class="flex flex-row gap-2">
                <ActiveRFQs />
                <ActiveRFQs />
                <ActiveRFQs />
                <ActiveRFQs />
                <ActiveRFQs />
            </div>

            <div class="flex flex-row gap-2 mb-2">
                <MonthlyRevenue />
                <ServiceDistribution />
                

            </div>
        </div>

    </div>


</div>

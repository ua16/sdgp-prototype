<script>
    import ActiveRFQs from "./applets/marshmallows/ActiveRFQs.svelte";
</script>

<div class="w-full h-full">
    <div
        class="text-black font-bold border-b-3 border-stone-300 bg-stone-100 p-2"
    >
        Dashboard
    </div>
    <div class="grid place-items-center bg-stone-200 h-100">
        <!-- All the stuff is contained in this -->
        <div class="w-9/10">
            <div>Good Day James</div>
            <!-- TODO : Maybe move this to another container at some point -->
            <div class="flex flex-row gap-2">
                <ActiveRFQs />
                <ActiveRFQs />
                <ActiveRFQs />
                <ActiveRFQs />
                <ActiveRFQs />
            </div>
        </div>
    </div>
</div>

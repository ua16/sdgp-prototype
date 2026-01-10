<script lang="ts">
    let { quotedata } = $props();
</script>

<div
    class="flex flex-col bg-stone-100 border-stone-300 border-2 p-3 text-stone-700 rounded-2xl"
>
    <div class="font-bold text-xl">
        <span>Shipment Route</span>
        <span class="text-sm float-end">Port-To-Port</span>
    </div>

    <div class="flex flex-row w-full items-center">
        <div class="flex flex-col w-1/3 items-center gap-2">
            <div class="text-sky-500">Origin</div>
            <div class="text-xl font-bold">{quotedata.origin}</div>
            <div class="text-fuchsia-500">Airport</div>
        </div>
        <!-- Some animation comes below -->
        <div class="w-1/3 h-px bg-[repeating-linear-gradient(to_right,#9ca3af_0,#9ca3af_6px,transparent_6px,transparent_16px)]"></div>
        <div class="flex flex-col w-1/3 items-center gap-2">
            <div class="text-sky-500">Destination</div>
            <div class="text-xl font-bold">{quotedata.destination}</div>
            <div class="text-fuchsia-500">Airport</div>
        </div>
    </div>
</div>
